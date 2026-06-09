import time
import allure
from appium.webdriver.common.appiumby import AppiumBy


class PaymentPage:

    # --------------------------------------------------
    # Locators (Page Factory Concept)
    # --------------------------------------------------
    PAYMENTS_MENU = (AppiumBy.ACCESSIBILITY_ID, "Payments")
    ENTER_PAYMENT_BTN = (AppiumBy.ACCESSIBILITY_ID, "Enter Payment")

    CLIENT_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(12)',
    )
    INVOICE_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(13)',
    )
    PAYMENT_METHOD_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(15)',
    )

    TRANSACTION_REF_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )
    PRIVATE_NOTES_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )
    SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, "Save")

    # --------------------------------------------------
    # Initialization
    # --------------------------------------------------
    def __init__(self, driver):
        self.driver = driver

    # --------------------------------------------------
    # Page Actions
    # --------------------------------------------------

    @allure.step("Open Payments section")
    def navigate_to_payments(self):
        print("[UI] Looking for Payments menu")
        element = self.driver.find_element(*self.PAYMENTS_MENU)
        assert element.is_displayed(), "Payments option not visible"

        print("[UI] Clicking Payments")
        element.click()
        time.sleep(0.5)

    @allure.step("Initiate Enter Payment")
    def click_enter_payment(self):
        print("[UI] Clicking 'Enter Payment' button")
        self.driver.find_element(*self.ENTER_PAYMENT_BTN).click()

    @allure.step("Select Client/Vendor")
    def select_client(self, client_name):
        print("[UI] Clicking Client dropdown")
        self.driver.find_element(*self.CLIENT_DROPDOWN).click()

        print(f"[UI] Clicking Client Name from JSON: {client_name}")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, client_name).click()

    @allure.step("Select Invoice via coordinate tap")
    def select_invoice_by_coordinates(self, x=360, y=210.5):
        print("[UI] Clicking Invoice dropdown")
        self.driver.find_element(*self.INVOICE_DROPDOWN).click()

        # Wait briefly for the dropdown animation to finish before tapping
        time.sleep(1)

        print(f"[UI] Tapping on coordinates ({x}, {y}) to select Invoice")
        self.driver.tap([(x, y)])

    @allure.step("Select Payment Method")
    def select_payment_method(self, payment_method):
        print("[UI] Clicking Payment Method dropdown")
        self.driver.find_element(*self.PAYMENT_METHOD_DROPDOWN).click()

        print(f"[UI] Clicking Payment Method from JSON: {payment_method}")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, payment_method).click()

    @allure.step("Enter Transaction Reference")
    def enter_transaction_reference(self, transaction_ref):
        print("[UI] Locating Transaction Reference field")
        field = self.driver.find_element(*self.TRANSACTION_REF_INPUT)

        print("[UI] Clicking Transaction Reference field")
        field.click()

        print(f"[UI] Sending keys to Transaction Reference: {transaction_ref}")
        field.send_keys(transaction_ref)

    @allure.step("Enter Private Notes")
    def enter_private_notes(self, private_notes):
        print("[UI] Locating Private Notes field")
        field = self.driver.find_element(*self.PRIVATE_NOTES_INPUT)

        print("[UI] Clicking Private Notes field")
        field.click()

        print(f"[UI] Sending keys to Private Notes: {private_notes}")
        field.send_keys(private_notes)

    @allure.step("Save Payment")
    def save_payment(self):
        print("[UI] Clicking 'Save' button")
        self.driver.find_element(*self.SAVE_BTN).click()

    @allure.step("Verify and Print Amounts")
    def verify_and_print_amounts(self, expected_amount, expected_applied):
        print("[UI] Locating Expected Amount field")
        amount_el = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{expected_amount}")',
        )
        print(
            f"VERIFICATION PRINT: Found Amount Element -> {amount_el.get_attribute('content-desc')}"
        )

        print("[UI] Locating Expected Applied Amount field")
        applied_el = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{expected_applied}")',
        )
        print(
            f"VERIFICATION PRINT: Found Applied Element -> {applied_el.get_attribute('content-desc')}"
        )
