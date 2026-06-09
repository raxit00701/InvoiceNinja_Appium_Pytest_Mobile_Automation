import time
import allure
from appium.webdriver.common.appiumby import AppiumBy


class InvoicePage:
    def __init__(self, driver):
        self.driver = driver

    # ==========================================
    # LOCATORS
    # ==========================================
    INVOICES_MENU = (AppiumBy.ACCESSIBILITY_ID, "Invoices")
    NEW_INVOICE_BTN = (AppiumBy.ACCESSIBILITY_ID, "New Invoice")

    # Tabs
    ITEMS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Items\nTab 3 of 5"]',
    )
    DETAILS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Details\nTab 1 of 5"]',
    )
    CONTACTS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Contacts\nTab 2 of 5"]',
    )
    NOTES_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Notes\nTab 4 of 5"]',
    )
    PDF_TAB = (AppiumBy.XPATH, '//android.view.View[@content-desc="PDF\nTab 5 of 5"]')

    # Items Tab Locators
    ADD_ITEM_BTN = (AppiumBy.ACCESSIBILITY_ID, "Add Item")
    ITEM_CHECKBOX = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.CheckBox").instance(0)',
    )
    SELECT_BTN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)',
    )
    DONE_BTN = (AppiumBy.ACCESSIBILITY_ID, "DONE")

    # Details Tab Locators
    CLIENT_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(22)',
    )
    USER_SELECTOR = (AppiumBy.ACCESSIBILITY_ID, "User")
    NEW_USER = (AppiumBy.ACCESSIBILITY_ID, "New User")
    INVOICE_DATE_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )
    PARTIAL_AMOUNT_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )
    DUE_DATE_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )
    SCROLL_TO_FREQ = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("1"))',
    )
    PO_NUMBER_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )
    DISCOUNT_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )
    DESIGN_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "Design")
    VENDOR_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(23)',
    )
    EXPENSE_ACCOUNT_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(22)',
    )
    EXPENSE_ACCOUNT_TEST = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("test").instance(0)',
    )

    # Notes Tab Locators
    TERMS_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )
    FOOTER_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )
    PUBLIC_NOTES_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )
    PRIVATE_NOTES_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    # PDF & Save Locators
    PDF_PREVIEW = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, "Save")
    INVOICE_AMOUNT_VERIFY = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().descriptionContains("Invoice Amount")',
    )
    BALANCE_DUE_VERIFY = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().descriptionContains("Balance Due")',
    )

    # ==========================================
    # HELPER METHOD
    # ==========================================
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    # ==========================================
    # PAGE ACTIONS
    # ==========================================
    def open_invoices_section(self):
        with allure.step("Open Invoices section"):
            print("[UI] Looking for Invoices menu")
            invoices_menu = self.get_element(self.INVOICES_MENU)
            assert invoices_menu.is_displayed(), "Invoices option not visible"

            print("[UI] Clicking Invoices")
            invoices_menu.click()
            time.sleep(2)

    def create_new_invoice(self):
        with allure.step("Create new invoice"):
            print("[UI] Clicking New Invoice")
            self.get_element(self.NEW_INVOICE_BTN).click()

    def add_invoice_item(self):
        with allure.step("Open Items tab"):
            print("[UI] Opening Items tab")
            self.get_element(self.ITEMS_TAB).click()

        with allure.step("Add invoice item"):
            print("[UI] Clicking Add Item")
            self.get_element(self.ADD_ITEM_BTN).click()

            print("[UI] Selecting item checkbox")
            self.get_element(self.ITEM_CHECKBOX).click()

            print("[UI] Clicking Select Button")
            self.get_element(self.SELECT_BTN).click()

            print("[UI] Clicking DONE")
            self.get_element(self.DONE_BTN).click()

    def fill_invoice_details(self, invoice):
        with allure.step("Open Details tab"):
            print("[UI] Opening Details tab")
            self.get_element(self.DETAILS_TAB).click()

        with allure.step("Select Client"):
            print("[UI] Opening Client dropdown")
            self.get_element(self.CLIENT_DROPDOWN).click()

            print(f"[UI] Selecting Client: {invoice['client']}")
            self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, invoice["client"]
            ).click()

        with allure.step("Select User"):
            print("[UI] Opening User selector")
            self.get_element(self.USER_SELECTOR).click()

            print("[UI] Selecting New User")
            self.get_element(self.NEW_USER).click()

        # --- 1 SECOND TIMERS INJECTED BETWEEN DATES & AMOUNTS ---
        with allure.step("Enter Invoice Date"):
            print(f"[UI] Entering Invoice Date = {invoice['invoice_date']}")
            invoice_date = self.get_element(self.INVOICE_DATE_INPUT)
            invoice_date.click()
            invoice_date.send_keys(invoice["invoice_date"])

        time.sleep(1)  # 1 sec delay before amount

        with allure.step("Enter Partial Amount"):
            print(f"[UI] Entering Partial Amount = {invoice['partial_amount']}")
            partial_amount = self.get_element(self.PARTIAL_AMOUNT_INPUT)
            partial_amount.click()
            partial_amount.send_keys(str(invoice["partial_amount"]))

        time.sleep(1)  # 1 sec delay before next date

        with allure.step("Enter Due Date"):
            print(f"[UI] Entering Due Date = {invoice['due_date']}")
            due_date = self.get_element(self.DUE_DATE_INPUT)
            due_date.click()
            due_date.send_keys(invoice["due_date"])

        time.sleep(1)  # 1 sec delay after dates

        with allure.step("Scroll until frequency section visible"):
            print("[UI] Scrolling to frequency section")
            self.get_element(self.SCROLL_TO_FREQ)

        with allure.step("Enter PO Number"):
            print(f"[UI] Entering PO Number = {invoice['po_number']}")
            po_number = self.get_element(self.PO_NUMBER_INPUT)
            po_number.click()
            po_number.send_keys(invoice["po_number"])

        with allure.step("Enter Discount"):
            print(f"[UI] Entering Discount = {invoice['discount']}")
            discount = self.get_element(self.DISCOUNT_INPUT)
            discount.click()
            discount.send_keys(str(invoice["discount"]))

        time.sleep(1)  # 1 sec delay after discount amount

        with allure.step("Select Design"):
            print("[UI] Opening Design dropdown")
            self.get_element(self.DESIGN_DROPDOWN).click()

            print(f"[UI] Selecting Design: {invoice['design']}")
            self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, invoice["design"]
            ).click()

        with allure.step("Select Vendor"):
            print("[UI] Opening Vendor dropdown")
            self.get_element(self.VENDOR_DROPDOWN).click()

            print(f"[UI] Selecting Vendor: {invoice['vendor']}")
            self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, invoice["vendor"]
            ).click()

        with allure.step("Select Expense Account"):
            print("[UI] Opening Expense Account dropdown")
            self.get_element(self.EXPENSE_ACCOUNT_DROPDOWN).click()

            print("[UI] Selecting Expense Account")
            self.get_element(self.EXPENSE_ACCOUNT_TEST).click()

    def open_contacts_tab(self):
        with allure.step("Open Contacts tab"):
            print("[UI] Opening Contacts tab")
            self.get_element(self.CONTACTS_TAB).click()

    def fill_invoice_notes(self, invoice):
        with allure.step("Open Notes tab"):
            print("[UI] Opening Notes tab")
            self.get_element(self.NOTES_TAB).click()

        with allure.step("Enter Notes"):
            print(f"[UI] Entering Invoice Terms = {invoice['invoice_terms']}")
            terms = self.get_element(self.TERMS_INPUT)
            terms.click()
            terms.send_keys(invoice["invoice_terms"])

            print(f"[UI] Entering Invoice Footer = {invoice['invoice_footer']}")
            footer = self.get_element(self.FOOTER_INPUT)
            footer.click()
            footer.send_keys(invoice["invoice_footer"])

            print(f"[UI] Entering Public Notes = {invoice['public_notes']}")
            public_notes = self.get_element(self.PUBLIC_NOTES_INPUT)
            public_notes.click()
            public_notes.send_keys(invoice["public_notes"])

            print(f"[UI] Entering Private Notes = {invoice['private_notes']}")
            private_notes = self.get_element(self.PRIVATE_NOTES_INPUT)
            private_notes.click()
            private_notes.send_keys(invoice["private_notes"])

    def verify_pdf_and_save(self):
        with allure.step("Open PDF tab"):
            print("[UI] Opening PDF tab")
            self.get_element(self.PDF_TAB).click()

        with allure.step("Verify PDF Preview"):
            print("[UI] Verifying PDF Preview is visible")
            pdf_preview = self.get_element(self.PDF_PREVIEW)
            assert pdf_preview.is_displayed(), "PDF Preview not displayed"

        with allure.step("Save Invoice"):
            print("[UI] Clicking Save")
            self.get_element(self.SAVE_BTN).click()

    def verify_invoice_totals(self):
        with allure.step("Verify Invoice Amount"):
            print("[UI] Verifying Invoice Amount is displayed")
            invoice_amount = self.get_element(self.INVOICE_AMOUNT_VERIFY)
            assert invoice_amount.is_displayed(), "Invoice Amount not displayed"
            print(
                f"[VERIFY] Invoice Amount Card:\n{invoice_amount.get_attribute('content-desc')}"
            )

        with allure.step("Verify Balance Due"):
            print("[UI] Verifying Balance Due is displayed")
            balance_due = self.get_element(self.BALANCE_DUE_VERIFY)
            assert balance_due.is_displayed(), "Balance Due not displayed"
            print(
                f"[VERIFY] Balance Due Card:\n{balance_due.get_attribute('content-desc')}"
            )

        print("[SUCCESS] Invoice created successfully")
