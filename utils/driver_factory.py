import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options

logger = logging.getLogger(__name__)


class DriverFactory:
    _driver = None

    @classmethod
    def create_driver(
        cls, env_config: dict, headless: bool = False
    ) -> webdriver.Remote:

        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = env_config.get("device_name", "emulator-5554")
        options.app_package = env_config.get("app_package", "com.invoiceninja.app")
        options.app_activity = env_config.get(
            "app_activity", "com.invoiceninja.app.MainActivity"
        )
        options.automation_name = "UiAutomator2"
        options.no_reset = env_config.get("no_reset", True)
        options.full_reset = env_config.get("full_reset", False)

        # Needed for typing special characters (emails, passwords, symbols)
        options.unicode_keyboard = env_config.get("unicode_keyboard", True)
        options.reset_keyboard = env_config.get("reset_keyboard", True)

        if headless:
            logger.info("Headless mode enabled.")

        appium_server = env_config.get("appium_server", "http://localhost:4723")
        logger.info(f"Connecting to Appium server: {appium_server}")

        cls._driver = webdriver.Remote(appium_server, options=options)
        cls._driver.implicitly_wait(env_config.get("implicit_wait", 15))
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
            logger.info("Driver session terminated.")
