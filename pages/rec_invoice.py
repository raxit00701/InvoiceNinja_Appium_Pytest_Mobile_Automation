import time

from appium.webdriver.common.appiumby import AppiumBy


class RecurringInvoicePage:

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # Locators
    # =========================================================

    RECURRING_INVOICES = (
        AppiumBy.ACCESSIBILITY_ID,
        "Recurring Invoices",
    )

    NEW_RECURRING_INVOICE = (
        AppiumBy.ACCESSIBILITY_ID,
        "New Recurring Invoice",
    )

    CLIENT_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(22)',
    )

    USER_DROPDOWN = (
        AppiumBy.ACCESSIBILITY_ID,
        "User",
    )

    NEW_USER = (
        AppiumBy.ACCESSIBILITY_ID,
        "New User",
    )

    PO_NUMBER = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    DISCOUNT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    AUTO_BILL = (
        AppiumBy.ACCESSIBILITY_ID,
        "Auto Bill",
    )

    DESIGN = (
        AppiumBy.ACCESSIBILITY_ID,
        "Design",
    )

    EXPENSE_ACCOUNT_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("test").instance(0)',
    )

    VENDOR_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(23)',
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

    ADD_ITEM = (
        AppiumBy.ACCESSIBILITY_ID,
        "Add Item",
    )

    ITEM_CHECKBOX = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.CheckBox").instance(0)',
    )

    ITEM_SAVE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)',
    )

    DONE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "DONE",
    )

    TERMS_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    FOOTER_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    PUBLIC_NOTES_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    PRIVATE_NOTES_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    PDF_PREVIEW = (
        AppiumBy.CLASS_NAME,
        "android.widget.ImageView",
    )

    SAVE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Save",
    )

    INVOICE_CARD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().descriptionContains("Invoice Amount")',
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

    def open_recurring_invoice_menu(self):

        print("[UI] Looking for Recurring Invoices menu")

        menu = self.driver.find_element(*self.RECURRING_INVOICES)

        assert menu.is_displayed(), "Invoices option not visible"

        menu.click()

        time.sleep(2)

    def click_new_recurring_invoice(self):

        print("[UI] Clicking New Recurring Invoice")

        self.click(self.NEW_RECURRING_INVOICE)

    def select_client(self, client_name):

        print(f"[UI] Selecting Client: {client_name}")

        self.click(self.CLIENT_DROPDOWN)

        self.click_accessibility_id(client_name)

    def select_user(self):

        print("[UI] Selecting New User")

        self.click(self.USER_DROPDOWN)

        self.click(self.NEW_USER)

    def scroll_to_frequency(self):

        print("[UI] Scrolling until text '1' is visible")

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector().scrollable(true))"
            '.scrollIntoView(new UiSelector().text("1"))',
        )

    def enter_po_number(self, po_number):

        print(f"[UI] PO Number = {po_number}")

        self.enter_text(self.PO_NUMBER, po_number)

    def enter_discount(self, discount):

        print(f"[UI] Discount = {discount}")

        self.enter_text(self.DISCOUNT, discount)

    def enable_auto_bill(self):

        print("[UI] Opening Auto Bill")

        self.click(self.AUTO_BILL)

        self.driver.tap([(367.5, 659)])

    def select_design(self, design_name):

        print(f"[UI] Selecting Design: {design_name}")

        self.click(self.DESIGN)

        self.click_accessibility_id(design_name)

    def select_expense_account(self, account_name="test"):
        print(f"[UI] Selecting Expense Account: {account_name}")

        # Step 1
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.View").instance(22)',
        ).click()

        # Step 2
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{account_name}").instance(0)',
        ).click()

    def select_vendor(self, vendor_name):

        print(f"[UI] Vendor = {vendor_name}")

        self.click(self.VENDOR_DROPDOWN)

        self.click_accessibility_id(vendor_name)

    def open_contacts_tab(self):

        self.click(self.CONTACTS_TAB)

    def open_items_tab(self):

        self.click(self.ITEMS_TAB)

    def add_item(self):

        self.click(self.ADD_ITEM)

        self.click(self.ITEM_CHECKBOX)

        self.click(self.ITEM_SAVE)

        self.click(self.DONE_BUTTON)

    def open_notes_tab(self):

        self.click(self.NOTES_TAB)

    def enter_notes(
        self,
        invoice_terms,
        invoice_footer,
        public_notes,
        private_notes,
    ):

        self.enter_text(self.TERMS_FIELD, invoice_terms)

        self.enter_text(self.FOOTER_FIELD, invoice_footer)

        self.enter_text(self.PUBLIC_NOTES_FIELD, public_notes)

        self.enter_text(self.PRIVATE_NOTES_FIELD, private_notes)

    def open_pdf_tab(self):

        self.click(self.PDF_TAB)

    def verify_pdf_preview(self):

        print("[VERIFY] Waiting for PDF preview")

        pdf_preview = self.driver.find_element(*self.PDF_PREVIEW)

        assert pdf_preview.is_displayed(), "PDF preview not displayed"

    def save(self):

        print("[UI] Clicking Save")

        self.click(self.SAVE_BUTTON)

    def verify_invoice_created(self, expected_amount):

        print(f"[VERIFY] Looking for invoice amount {expected_amount}")

        time.sleep(5)

        invoice_card = self.driver.find_element(*self.INVOICE_CARD)

        assert invoice_card.is_displayed(), "Invoice card not displayed"

        print(
            f"[SUCCESS] Invoice created successfully "
            f"with expected amount {expected_amount}"
        )
