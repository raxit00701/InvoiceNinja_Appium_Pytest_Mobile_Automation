import pytest
import allure
import json
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

# Load test data
with open("data/login_data.json") as f:
    test_data = json.load(f)


@allure.epic("Invoice Ninja")
@allure.feature("Login")
class TestLogin:
    @allure.title("Login with self hosted server")
    @allure.description("Validate login flow for self-hosted Invoice Ninja app")
    @allure.severity(allure.severity_level.CRITICAL)
    # Priority Marker
    @pytest.mark.order(1)
    @pytest.mark.reset_app
    @pytest.mark.parametrize("login", test_data["login"])
    def test_login(self, driver, login):

        print("\n========== LOGIN TEST STARTED ==========")

        # Step 1 - Click Self-Hosted
        with allure.step("Click on Self-Hosted"):
            print("[UI] Looking for Self-Hosted button")

            self_hosted = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Self-Hosted")

            assert self_hosted.is_displayed(), "Self-Hosted button not visible"

            print("[UI] Clicking Self-Hosted")

            self_hosted.click()

            time.sleep(2)

        # Step 2 - Enter Email
        with allure.step("Enter email"):
            print("[UI] Locating Email field")

            email_field = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(0)',
            )

            assert email_field.is_displayed(), "Email field not visible"

            print(f"[UI] Entering Email: {login['email']}")

            email_field.click()
            email_field.clear()
            email_field.send_keys(login["email"])

            time.sleep(1)

        # Step 3 - Enter Password
        with allure.step("Enter password"):
            print("[UI] Locating Password field")

            password_field = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(1)',
            )

            assert password_field.is_displayed(), "Password field not visible"

            print("[UI] Entering Password")

            password_field.click()
            password_field.clear()
            password_field.send_keys(login["password"])

        # Step 4 - Fast Scroll Until Login Button Visible
        with allure.step("Fast scroll to Login with email button"):
            print("[UI] Starting fast scroll")

            login_button_visible = False

            for attempt in range(5):
                try:
                    login_button = driver.find_element(
                        AppiumBy.ACCESSIBILITY_ID, "Login with email"
                    )

                    if login_button.is_displayed():
                        login_button_visible = True
                        print("[UI] Login with email button is visible")
                        break

                except NoSuchElementException:
                    print(f"[UI] Fast scroll attempt {attempt + 1}")

                    size = driver.get_window_size()

                    start_x = size["width"] // 2

                    # Faster & longer swipe
                    start_y = int(size["height"] * 0.90)

                    end_y = int(size["height"] * 0.20)

                    driver.swipe(start_x, start_y, start_x, end_y, 300)

                    time.sleep(1)

            assert (
                login_button_visible
            ), "Login with email button not found after scrolling"

        # Step 5 - Enter Server URL
        with allure.step("Enter server URL"):
            print("[UI] Locating Server URL field")

            server_field = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(3)',
            )

            assert server_field.is_displayed(), "Server URL field not visible"

            print(f"[UI] Entering Server URL: {login['server_url']}")

            server_field.click()
            server_field.clear()
            server_field.send_keys(login["server_url"])

            time.sleep(1)

        # Step 6 - Click Login with email
        with allure.step("Click Login with email"):
            print("[UI] Clicking Login with email")

            login_button = driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, "Login with email"
            )

            assert login_button.is_displayed(), "Login button not visible"

            login_button.click()

            time.sleep(5)

        # Step 7 - Verify Welcome Popup
        with allure.step("Verify welcome popup"):
            print("[UI] Verifying Welcome popup")

            welcome_popup = driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, "Welcome to Invoice Ninja"
            )

            assert welcome_popup.is_displayed(), "Welcome popup not displayed"

            print("[UI] Welcome popup displayed successfully")

            time.sleep(2)

        # Step 8 - Close Popup
        with allure.step("Close welcome popup"):
            print("[UI] Clicking CLOSE button")

            close_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CLOSE")

            assert close_button.is_displayed(), "Close button not visible"

            close_button.click()

            time.sleep(2)

        print("========== LOGIN TEST COMPLETED ==========\n")
