import os
import base64
import logging
import allure
from datetime import datetime

logger = logging.getLogger(__name__)

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots")
VIDEO_DIR = os.path.join(os.path.dirname(__file__), "..", "reports", "videos")


# ════════════════════════════════════════════════════════
# SCREENSHOTS
# ════════════════════════════════════════════════════════


def take_screenshot(driver, name: str = "screenshot"):
    """Save a screenshot to disk and attach it to the Allure report."""
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(SCREENSHOT_DIR, f"{name}_{timestamp}.png")

    try:
        driver.save_screenshot(filepath)
        logger.info(f"Screenshot saved: {filepath}")
        with open(filepath, "rb") as f:
            allure.attach(
                f.read(), name=name, attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        logger.error(f"Failed to take screenshot: {e}")


# ════════════════════════════════════════════════════════
# VIDEO RECORDING  (uses Appium built-in — no extra libs)
# ════════════════════════════════════════════════════════


def start_recording(driver):
    """
    Start screen recording via Appium.
    Call this at the beginning of a test.

    Usage in conftest.py:
        start_recording(driver)
    """
    try:
        driver.start_recording_screen()
        logger.info("Screen recording started.")
    except Exception as e:
        logger.warning(f"Could not start recording: {e}")


def stop_recording(driver, name: str = "recording"):
    """
    Stop screen recording, save to disk, and attach to Allure report.
    Call this at the end of a test (pass or fail).

    Usage in conftest.py:
        stop_recording(driver, name="test_signup")
    """
    os.makedirs(VIDEO_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(VIDEO_DIR, f"{name}_{timestamp}.mp4")

    try:
        # Appium returns the video as a base64 encoded string
        video_base64 = driver.stop_recording_screen()
        video_bytes = base64.b64decode(video_base64)

        with open(filepath, "wb") as f:
            f.write(video_bytes)
        logger.info(f"Video saved: {filepath}")

        allure.attach(
            video_bytes, name=name, attachment_type=allure.attachment_type.MP4
        )
    except Exception as e:
        logger.error(f"Failed to stop/save recording: {e}")


# ════════════════════════════════════════════════════════
# LOGGING
# ════════════════════════════════════════════════════════


def setup_logging(enable: bool = True, level: int = logging.DEBUG):
    """Set up console + file logging."""
    if not enable:
        return

    log_dir = os.path.join(os.path.dirname(__file__), "..", "reports", "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(
        log_dir, f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )
    logger.info(f"Logging initialized: {log_file}")
