import time

from appium.webdriver.common.appiumby import AppiumBy


class PurchaseOrdersPage:

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # Locators
    # =========================================================

    NEW_PURCHASE_ORDER = (
        AppiumBy.ACCESSIBILITY_ID,
        "New Purchase Order",
    )

    USER_DROPDOWN = (
        AppiumBy.ACCESSIBILITY_ID,
        "User",
    )

    CONTACTS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Contacts\nTab 2 of 5"]',
    )

    ITEMS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Items\nTab 3 of 5"]',
    )

    NOTES_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Notes\nTab 4 of 5"]',
    )

    PDF_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="PDF\nTab 5 of 5"]',
    )

    SAVE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Save",
    )

    ADD_ITEM_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Add Item",
    )

    # =========================================================
    # Generic Helpers
    # =========================================================

    def click(self, locator):

        self.driver.find_element(*locator).click()

        time.sleep(0.3)

    # =========================================================
    # Actions
    # =========================================================

    def open_purchase_orders_menu(self):

        print("[UI] Looking for Purchase Orders menu")

        purchase_orders_menu = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector().scrollable(true))"
            '.scrollIntoView(new UiSelector().description("Purchase Orders"))',
        )

        assert (
            purchase_orders_menu.is_displayed()
        ), "Purchase Orders option not visible even after scrolling"

        print("[UI] Clicking Purchase Orders")

        purchase_orders_menu.click()

        time.sleep(2)

    def click_new_purchase_order(self):

        print("[UI] Looking for New Purchase Order button")

        new_purchase_order = self.driver.find_element(*self.NEW_PURCHASE_ORDER)

        assert new_purchase_order.is_displayed()

        print("[UI] Clicking New Purchase Order")

        new_purchase_order.click()

        time.sleep(0.3)

    def select_vendor(self, vendor_name):

        print("[UI] Opening Vendor dropdown")

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.View").instance(22)',
        ).click()

        print(f"[UI] Selecting Vendor: {vendor_name}")

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            vendor_name,
        ).click()

        time.sleep(0.3)

    def select_user(self, user_name):

        print("[UI] Opening User dropdown")

        self.driver.find_element(*self.USER_DROPDOWN).click()

        print(f"[UI] Selecting User: {user_name}")

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            user_name,
        ).click()

        time.sleep(0.3)

    def enter_due_date(self, due_date):

        print(f"[UI] Entering Due Date: {due_date}")

        field = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)',
        )

        field.click()
        field.send_keys(due_date)

        time.sleep(0.3)

    def enter_discount(self, discount):

        print(f"[UI] Entering Discount: {discount}")

        field = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(2)',
        )

        field.click()
        field.send_keys(str(discount))

        time.sleep(0.3)

    def enter_shipping_cost(self, shipping_cost):

        print(f"[UI] Entering Shipping Cost: {shipping_cost}")

        field = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(3)',
        )

        field.click()
        field.send_keys(str(shipping_cost))

        time.sleep(0.3)

    def scroll_to_item_section(self):

        print("[UI] Scrolling until item section is visible")

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector().scrollable(true))"
            '.scrollIntoView(new UiSelector().text("1"))',
        )

        time.sleep(0.3)

    def select_design(self, design_name):

        print(f"[UI] Selecting Design: {design_name}")

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Design",
        ).click()

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            design_name,
        ).click()

        time.sleep(0.3)

    def select_client(self, client_name):

        print("[UI] Opening Client dropdown")

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.View").instance(23)',
        ).click()

        print(f"[UI] Selecting Client: {client_name}")

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            client_name,
        ).click()

        time.sleep(0.3)

    def select_expense_account(self, expense_account):

        print(f"[UI] Selecting Expense Account: {expense_account}")

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.View").instance(22)',
        ).click()

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{expense_account}").instance(0)',
        ).click()

        time.sleep(0.3)

    def open_contacts_tab(self):

        print("[UI] Navigating to Contacts tab")

        self.click(self.CONTACTS_TAB)

    def open_items_tab(self):

        print("[UI] Navigating to Items tab")

        self.click(self.ITEMS_TAB)

    def add_item(self):

        print("[UI] Adding item")

        self.driver.find_element(*self.ADD_ITEM_BUTTON).click()

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.CheckBox").instance(2)',
        ).click()

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.Button").instance(1)',
        ).click()

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "DONE",
        ).click()

        time.sleep(0.3)

    def open_notes_tab(self):

        print("[UI] Navigating to Notes tab")

        self.click(self.NOTES_TAB)

    def enter_notes(
        self,
        invoice_terms,
        invoice_footer,
        public_notes,
        private_notes,
    ):

        print(f"[UI] Entering Invoice Terms: {invoice_terms}")

        field = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(0)',
        )

        field.click()
        field.send_keys(invoice_terms)

        time.sleep(0.3)

        print(f"[UI] Entering Invoice Footer: {invoice_footer}")

        field = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)',
        )

        field.click()
        field.send_keys(invoice_footer)

        time.sleep(0.3)

        print(f"[UI] Entering Public Notes: {public_notes}")

        field = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(2)',
        )

        field.click()
        field.send_keys(public_notes)

        time.sleep(0.3)

        print(f"[UI] Entering Private Notes: {private_notes}")

        field = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(3)',
        )

        field.click()
        field.send_keys(private_notes)

        time.sleep(0.3)

    def open_pdf_tab(self):

        print("[UI] Navigating to PDF tab")

        self.click(self.PDF_TAB)

        time.sleep(3)

    def save(self):

        print("[UI] Clicking Save button")

        self.driver.find_element(*self.SAVE_BUTTON).click()

        time.sleep(3)

    def verify_purchase_order_created(self, expected_amount):

        print(f"[UI] Verifying Purchase Order Amount: {expected_amount}")

        purchase_order_card = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().descriptionContains("{expected_amount}")',
        )

        assert (
            purchase_order_card.is_displayed()
        ), f"Purchase Order with amount {expected_amount} not found"

        print("[PASS] Purchase Order created successfully")
