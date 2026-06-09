import time

from appium.webdriver.common.appiumby import AppiumBy


class RecurringExpensePage:

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # Locators
    # =========================================================

    MENU_SIDEBAR = (AppiumBy.ACCESSIBILITY_ID, "Menu Sidebar")
    NEW_RECURRING_EXPENSE = (
        AppiumBy.ACCESSIBILITY_ID,
        "New Recurring Expense",
    )

    NOTES_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Notes\nTab 2 of 3"]',
    )

    SETTINGS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Settings\nTab 3 of 3"]',
    )

    SAVE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Save",
    )

    AMOUNT_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    PUBLIC_NOTE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    PRIVATE_NOTE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    CUSTOMER_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(19)',
    )

    VENDOR_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(20)',
    )

    EXPENSE_ACCOUNT_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(21)',
    )

    CATEGORY_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(22)',
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
        field.send_keys(value)

        time.sleep(0.3)

    # =========================================================
    # Page Actions
    # =========================================================

    def open_recurring_expense_menu(self):

        print("[UI] Looking for Recurring Expense menu")

        recurring_expense_menu = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector().scrollable(true))"
            '.scrollIntoView(new UiSelector().description("Recurring Expenses"))',
        )

        assert recurring_expense_menu.is_displayed()

        print("[UI] Clicking Recurring Expense")

        recurring_expense_menu.click()

        time.sleep(0.3)

    def click_new_recurring_expense(self):

        print("[UI] Clicking New Recurring Expense")

        self.click(self.NEW_RECURRING_EXPENSE)

    def select_customer(self, customer_name):

        print(f"[UI] Selecting Customer: {customer_name}")

        self.click(self.CUSTOMER_DROPDOWN)

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            customer_name,
        ).click()

        time.sleep(0.3)

    def select_vendor(self, vendor_name):

        print(f"[UI] Selecting Vendor: {vendor_name}")

        self.click(self.VENDOR_DROPDOWN)

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            vendor_name,
        ).click()

        time.sleep(0.3)

    def select_expense_account(self, expense_account):

        print(f"[UI] Selecting Expense Account: {expense_account}")

        self.click(self.EXPENSE_ACCOUNT_DROPDOWN)

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{expense_account}").instance(0)',
        ).click()

        time.sleep(0.3)

    def select_category(self, category_name):

        print(f"[UI] Selecting Category: {category_name}")

        self.click(self.CATEGORY_DROPDOWN)

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            category_name,
        ).click()

        time.sleep(0.3)

    def select_user(self, user_name):

        print(f"[UI] Selecting User: {user_name}")

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "User",
        ).click()

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            user_name,
        ).click()

        time.sleep(0.3)

    def enter_amount(self, amount):

        print(f"[UI] Entering Amount: {amount}")

        self.enter_text(self.AMOUNT_FIELD, str(amount))

    def add_notes(self, public_note, private_note):

        print("[UI] Navigating to Notes tab")

        self.click(self.NOTES_TAB)

        print(f"[UI] Entering Public Note: {public_note}")

        self.enter_text(self.PUBLIC_NOTE_FIELD, public_note)

        print(f"[UI] Entering Private Note: {private_note}")

        self.enter_text(self.PRIVATE_NOTE_FIELD, private_note)

    def open_settings_tab(self):

        print("[UI] Navigating to Settings tab")

        self.click(self.SETTINGS_TAB)

    def enable_document_visibility(self):

        print("[UI] Tapping document visibility toggle at coordinates (579,716)")

        self.driver.tap([(579, 716)])

        time.sleep(0.3)

    def save(self):

        print("[UI] Clicking Save")

        self.click(self.SAVE_BUTTON)

        time.sleep(3)

    def verify_recurring_expense_created(self, amount):

        amount_text = f"${float(amount):.2f}"

        print(f"[UI] Verifying amount card: {amount_text}")

        expense_card = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().descriptionContains("{amount_text}")',
        )

        assert (
            expense_card.is_displayed()
        ), f"Recurring expense with amount {amount_text} not found"

        print("[PASS] Recurring Expense created successfully")
