import os
import pytest
import allure
import logging
import shutil

from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.driver_factory import DriverFactory
from utils.json_reader import JSONReader
from utils.reset_manager import (
    ResetManager,
    APP_LOAD_TIMEOUT,
    APP_READY_SELECTOR,
)
from utils.reporting_utils import (
    take_screenshot,
    setup_logging,
    start_recording,
    stop_recording,
)
from utils.db_utils import DBUtils

logger = logging.getLogger(__name__)

CONFIG_DIR = os.path.join(
    os.path.dirname(__file__),
    "config",
    "env",
)

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "data",
    "login_data.json",
)

# ─────────────────────────────────────────────
# Read boolean toggles from pytest.ini
# ─────────────────────────────────────────────


def is_enabled(config, key: str) -> bool:
    """Read a true/false value from pytest.ini by key name."""

    value = config.getini(key)

    return str(value).strip().lower() == "true"


# ─────────────────────────────────────────────
# Register pytest.ini keys + markers
# ─────────────────────────────────────────────


def pytest_addoption(parser):

    parser.addoption(
        "--env",
        action="store",
        default="test",
        choices=["test", "stage", "prod"],
        help="Environment to run tests against",
    )

    # Kept for CLI override capability
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run in headless mode via command line",
    )

    # Register ini keys
    parser.addini(
        "screenshots",
        default="true",
        help="Capture screenshots on failure",
    )

    parser.addini(
        "logs",
        default="true",
        help="Enable logging to file",
    )

    parser.addini(
        "video",
        default="false",
        help="Record video — saved only on failure",
    )

    parser.addini(
        "headless",
        default="false",
        help="Run Appium in headless mode from pytest.ini",
    )


def pytest_configure(config):

    config.addinivalue_line(
        "markers",
        "reset_app: Reset app and clear data",
    )

    config.addinivalue_line(
        "markers",
        "restart_app: Restart app without clearing data",
    )


# ─────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────


@pytest.fixture(scope="session")
def env_config(request):

    env = request.config.getoption("--env")

    path = os.path.join(
        CONFIG_DIR,
        f"{env}.json",
    )

    logger.info(f"Loading config: {path}")

    return JSONReader.load(path)


@pytest.fixture(scope="session")
def test_data():

    return JSONReader.load(DATA_PATH)


@pytest.fixture(scope="session")
def driver(request, env_config):

    setup_logging(
        enable=is_enabled(
            request.config,
            "logs",
        )
    )

    # Check both pytest.ini and command line arguments
    run_headless = is_enabled(request.config, "headless") or request.config.getoption(
        "--headless"
    )

    drv = DriverFactory.create_driver(
        env_config,
        headless=run_headless,
    )

    try:

        WebDriverWait(
            drv,
            APP_LOAD_TIMEOUT,
        ).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    APP_READY_SELECTOR,
                )
            )
        )

        logger.info("App loaded successfully.")

    except TimeoutException:

        logger.warning("App load timed out — proceeding anyway.")

    yield drv

    # ---------------------------------------------------------
    # Safe Driver Teardown
    # ---------------------------------------------------------

    try:

        DriverFactory.quit_driver()

        logger.info("Driver session terminated.")

    except Exception as e:

        logger.warning(f"Driver quit failed: {e}")


@pytest.fixture(scope="session")
def db():

    database = DBUtils()

    database.connect()

    yield database

    database.disconnect()


@pytest.fixture(autouse=True)
def handle_reset(request, driver):

    # Full reset
    if request.node.get_closest_marker("reset_app"):

        ResetManager(driver).reset_app()

    # Restart only
    elif request.node.get_closest_marker("restart_app"):

        ResetManager(driver).restart_app()

    yield


# ─────────────────────────────────────────────
# Video Handling
# ─────────────────────────────────────────────


@pytest.fixture(autouse=True)
def handle_video(request, driver):

    record = is_enabled(
        request.config,
        "video",
    )

    if record:

        start_recording(driver)

    yield

    if not record:
        return

    rep = getattr(
        request.node,
        "rep_call",
        None,
    )

    # ---------------------------------------------------------
    # Save video on failure
    # ---------------------------------------------------------

    if rep and rep.failed:

        logger.info(f"Test failed — saving video: " f"{request.node.name}")

        try:

            stop_recording(
                driver,
                name=request.node.name,
            )

        except Exception as e:

            logger.warning(f"Failed to save video: {e}")

    # ---------------------------------------------------------
    # Discard video on pass
    # ---------------------------------------------------------

    else:

        try:

            driver.stop_recording_screen()

        except Exception as e:

            logger.warning(f"Failed to stop recording: {e}")


# ─────────────────────────────────────────────
# Screenshots
# ─────────────────────────────────────────────


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call,
):

    outcome = yield

    report = outcome.get_result()

    # Required for video fixture
    setattr(
        item,
        "rep_" + report.when,
        report,
    )

    if report.when == "call" and report.failed:

        if not is_enabled(
            item.config,
            "screenshots",
        ):
            return

        driver = item.funcargs.get("driver")

        if driver:

            try:

                take_screenshot(
                    driver,
                    name=f"FAILED_{item.name}",
                )

            except Exception as e:

                logger.warning(f"Screenshot failed: {e}")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """
    Save history, clean allure-results, and restore history.
    """
    allure_dir = session.config.getoption("--alluredir")
    report_dir = "reports/allure-report"  # Where the permanent report is generated
    history_src = os.path.join(report_dir, "history")
    history_dst = os.path.join(allure_dir, "history")

    # 1. If a previous report exists, copy its history to the results folder
    if os.path.exists(history_src):
        logger.info(f"Preserving Allure history from {history_src}")
        os.makedirs(allure_dir, exist_ok=True)
        # Copy history folder to the directory we are about to fill with new results
        if os.path.exists(history_dst):
            shutil.rmtree(history_dst)
        shutil.copytree(history_src, history_dst)

    # 2. Clean allure-results directory (excluding the history folder we just copied)
    if allure_dir and os.path.exists(allure_dir):
        logger.info(f"Cleaning existing allure results in: {allure_dir}")
        for item in os.listdir(allure_dir):
            item_path = os.path.join(allure_dir, item)
            if item != "history":  # DO NOT delete the history folder
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """
    Generate environment.properties file for Allure dashboard.
    """
    allure_dir = session.config.getoption("--alluredir")

    if allure_dir and os.path.exists(allure_dir):
        env = session.config.getoption("--env")

        # Get the set of markers actually used in this session
        used_markers = set()
        for item in session.items:
            used_markers.update(item.keywords.keys())

        # Filter against your target groups
        target_groups = ["smoke", "reg", "login"]
        active_groups = [m for m in target_groups if m in used_markers]

        env_properties = [
            f"Environment = {env}",
            f"Test_Groups = {', '.join(active_groups) if active_groups else 'None'}",
        ]

        with open(os.path.join(allure_dir, "environment.properties"), "w") as f:
            f.write("\n".join(env_properties))
        logger.info(
            f"Generated Allure environment.properties for {env} with groups: {active_groups}"
        )
