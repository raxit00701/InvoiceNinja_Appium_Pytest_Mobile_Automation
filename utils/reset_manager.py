import logging
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)

APP_LOAD_TIMEOUT = 30
APP_STABILIZATION_TIME = 5

APP_READY_SELECTOR = "new UiSelector().clickable(true)"


class ResetManager:

    def __init__(self, driver):
        self.driver = driver

    def reset_app(self):
        """
        Clears all app data (logs out user, wipes session)
        then relaunches the app.
        """

        app_package = self.driver.capabilities.get(
            "appPackage"
        ) or self.driver.capabilities.get("appium:appPackage")

        if app_package:

            logger.info(f"Clearing app data: {app_package}")

            self.driver.terminate_app(app_package)

            self.driver.execute_script("mobile: clearApp", {"appId": app_package})

            self.driver.activate_app(app_package)

        else:
            logger.warning("App package not found — using reset() fallback.")

            self.driver.reset()

        self._wait_for_app_ready()

    def restart_app(self):
        """
        Restarts app WITHOUT clearing data.
        User session remains logged in.
        """

        app_package = self.driver.capabilities.get(
            "appPackage"
        ) or self.driver.capabilities.get("appium:appPackage")

        if app_package:

            logger.info(f"Restarting app: {app_package}")

            self.driver.terminate_app(app_package)

            # Small wait before relaunch
            time.sleep(2)

            self.driver.activate_app(app_package)

        else:
            logger.warning("App package not found — using reset() fallback.")

            self.driver.reset()

        self._wait_for_app_ready()

    def _wait_for_app_ready(self):

        logger.info(f"Waiting up to {APP_LOAD_TIMEOUT}s for app to load...")

        try:

            WebDriverWait(self.driver, APP_LOAD_TIMEOUT).until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, APP_READY_SELECTOR)
                )
            )

            logger.info("App is ready.")

            # ADD THIS STABILIZATION WAIT
            logger.info(
                f"Waiting {APP_STABILIZATION_TIME}s " f"for app stabilization..."
            )

            time.sleep(APP_STABILIZATION_TIME)

            logger.info("App stabilization completed.")

        except TimeoutException:

            logger.warning("App load timed out — proceeding anyway.")
