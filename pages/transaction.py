import time

from appium.webdriver.common.appiumby import AppiumBy


class TransactionPage:

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # Locators
    # =========================================================

    NEW_TRANSACTION = (
        AppiumBy.ACCESSIBILITY_ID,
        "New Transaction",
    )

    CLIENT_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(13)',
    )

    CREATE_NEW = (
        AppiumBy.ACCESSIBILITY_ID,
        "Create New",
    )

    CLIENT_NAME_FIELD = (
        AppiumBy.CLASS_NAME,
        "android.widget.EditText",
    )

    SAVE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Save",
    )

    BACK_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(5)',
    )

    AMOUNT_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    DESCRIPTION_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    # =========================================================
    # Generic Methods
    # =========================================================

    def click(self, locator):

        self.driver.find_element(*locator).click()

        time.sleep(0.3)

    def enter_text(self, locator, value):

        field = self.driver.find_element(*locator)

        field.click()

        field.clear()

        field.send_keys(str(value))

        time.sleep(0.3)

    def click_accessibility_id(self, value):

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            value,
        ).click()

        time.sleep(0.3)

    # =========================================================
    # Page Actions
    # =========================================================

    def open_transactions_menu(self):

        print("[UI] Scrolling until Transactions is visible")

        transactions_menu = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector().scrollable(true))"
            '.scrollIntoView(new UiSelector().description("Transactions"))',
        )

        assert transactions_menu.is_displayed(), "Transactions option not visible"

        print("[UI] Clicking Transactions")

        transactions_menu.click()

        time.sleep(2)

    # =========================================================
    # Client Creation
    # =========================================================

    def create_client(self, client_name):

        print("[UI] Clicking New Transaction")

        self.click(self.NEW_TRANSACTION)

        self.click(self.CLIENT_DROPDOWN)

        self.click(self.CREATE_NEW)

        print(f"[UI] Creating Client: {client_name}")

        self.enter_text(
            self.CLIENT_NAME_FIELD,
            client_name,
        )

        self.click(self.SAVE_BUTTON)

        print(f"[UI] Client created: {client_name}")

    # =========================================================
    # Transaction Creation
    # =========================================================

    def start_new_transaction(self):

        self.click(self.BACK_BUTTON)

        self.click(self.NEW_TRANSACTION)

    def select_transaction_type(self, transaction_type):

        print(f"[UI] Selecting Transaction Type: {transaction_type}")

        self.driver.tap([(360, 270)])

        self.click_accessibility_id(transaction_type)

    def enter_amount(self, amount):

        print(f"[UI] Amount = {amount}")

        self.enter_text(
            self.AMOUNT_FIELD,
            amount,
        )

    def select_client(self, client_name):

        print("[UI] Opening client selector")

        self.click(self.CLIENT_DROPDOWN)

        print(f"[UI] Selecting client: {client_name}")

        self.click_accessibility_id(client_name)

    def enter_description(self, description):

        print(f"[UI] Description = {description}")

        self.enter_text(
            self.DESCRIPTION_FIELD,
            description,
        )

    def save_transaction(self):

        print("[UI] Clicking Save")

        self.click(self.SAVE_BUTTON)

    # =========================================================
    # Complete Flow
    # =========================================================

    def create_transaction(
        self,
        client_name,
        transaction_type,
        amount,
        description,
    ):

        self.start_new_transaction()

        self.select_transaction_type(transaction_type)

        self.enter_amount(amount)

        self.select_client(client_name)

        self.enter_description(description)

        self.save_transaction()

        print(
            f"[SUCCESS] Transaction created | "
            f"Client: {client_name} | "
            f"Type: {transaction_type} | "
            f"Amount: {amount}"
        )
