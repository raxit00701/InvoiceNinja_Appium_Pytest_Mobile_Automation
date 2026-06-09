import time

from appium.webdriver.common.appiumby import AppiumBy


class VendorsPage:

    def __init__(self, driver):

        self.driver = driver

    # ---------------------------------------------------------
    # Locators
    # ---------------------------------------------------------

    VENDORS_MENU = (AppiumBy.ACCESSIBILITY_ID, "Vendors")

    NEW_VENDOR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "New Vendor")

    USER_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "User")

    NEW_USER = (AppiumBy.ACCESSIBILITY_ID, "New User")

    TAX_EXEMPT = (AppiumBy.ACCESSIBILITY_ID, "Tax Exempt")

    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Save")

    UPLOAD_FILES = (AppiumBy.ACCESSIBILITY_ID, "Upload Files")

    # ---------------------------------------------------------
    # Actions
    # ---------------------------------------------------------

    def click_vendors(self):

        print("[UI] Clicking Vendors")

        vendors = self.driver.find_element(*self.VENDORS_MENU)

        vendors.click()

        time.sleep(0.5)

    def click_new_vendor(self):

        print("[UI] Clicking New Vendor")

        new_vendor = self.driver.find_element(*self.NEW_VENDOR_BUTTON)

        new_vendor.click()

        time.sleep(0.5)

    def enter_vendor_name(self, vendor_name_value):

        print("[UI] Entering Vendor Name")

        vendor_name = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(0)',
        )

        vendor_name.click()

        vendor_name.send_keys(vendor_name_value)

        time.sleep(0.25)

    def select_user(self):

        print("[UI] Selecting User")

        user_dropdown = self.driver.find_element(*self.USER_DROPDOWN)

        user_dropdown.click()

        time.sleep(0.25)

        new_user = self.driver.find_element(*self.NEW_USER)

        new_user.click()

        time.sleep(0.25)

    def enter_id_number(self, id_value):

        print("[UI] Entering ID Number")

        id_number = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)',
        )

        id_number.click()

        id_number.send_keys(id_value)

        time.sleep(0.25)

    def enter_vat_number(self, vat_value):

        print("[UI] Entering VAT Number")

        vat_number = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(2)',
        )

        vat_number.click()

        vat_number.send_keys(vat_value)

        time.sleep(0.25)

    def enter_website(self, website_value):

        print("[UI] Entered Website")

        website = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(3)',
        )

        website.click()

        website.send_keys(website_value)

        time.sleep(0.25)

    def enter_phone(self, phone_value):

        print("[UI] Entered Phone")

        phone = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(4)',
        )

        phone.click()

        phone.send_keys(phone_value)

        time.sleep(0.25)

    def click_tax_exempt(self):

        print("[UI] Clicked Tax Exempt")

        tax_exempt = self.driver.find_element(*self.TAX_EXEMPT)

        tax_exempt.click()

        time.sleep(0.25)

    def open_contacts_tab(self):

        print("[UI] Opening Contacts Tab")

        contacts_tab = self.driver.find_element(
            AppiumBy.XPATH, '//*[contains(@content-desc,"Contacts")]'
        )

        contacts_tab.click()

        time.sleep(0.25)

    def enter_contact_details(
        self, first_name_value, last_name_value, email_value, phone_value
    ):

        print("[UI] Entered first name, last name email address and contact number")

        first_name = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(0)',
        )

        first_name.click()

        first_name.send_keys(first_name_value)

        time.sleep(0.25)

        last_name = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)',
        )

        last_name.click()

        last_name.send_keys(last_name_value)

        time.sleep(0.25)

        email = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(2)',
        )

        email.click()

        email.send_keys(email_value)

        time.sleep(0.25)

        contact_phone = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(3)',
        )

        contact_phone.click()

        contact_phone.send_keys(phone_value)

        time.sleep(0.25)

    def open_notes_tab(self):

        print("[UI] Opening Notes Tab")

        notes_tab = self.driver.find_element(
            AppiumBy.XPATH, '//*[contains(@content-desc,"Notes")]'
        )

        notes_tab.click()

        time.sleep(0.25)

    def enter_notes(self, public_value, private_value):

        print("[UI] Entered public and private notes")

        public_notes = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(0)',
        )

        public_notes.click()

        public_notes.send_keys(public_value)

        time.sleep(0.25)

        private_notes = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)',
        )

        private_notes.click()

        private_notes.send_keys(private_value)

        time.sleep(0.25)

    def open_address_tab(self):

        print("[UI] Opening Andress Tab")

        address_tab = self.driver.find_element(
            AppiumBy.XPATH, '//*[contains(@content-desc,"Address")]'
        )

        address_tab.click()

        time.sleep(0.25)

    def enter_address(
        self, address1_value, address2_value, city_value, state_value, postal_code_value
    ):

        print("[UI] Entered Address Details")

        address1 = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(0)',
        )

        address1.click()

        address1.send_keys(address1_value)

        time.sleep(0.25)

        address2 = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)',
        )

        address2.click()

        address2.send_keys(address2_value)

        time.sleep(0.25)

        city = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(2)',
        )

        city.click()

        city.send_keys(city_value)

        time.sleep(0.25)

        state = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(3)',
        )

        state.click()

        state.send_keys(state_value)

        time.sleep(0.25)

        postal_code = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(4)',
        )

        postal_code.click()

        postal_code.send_keys(postal_code_value)

        time.sleep(0.25)

    def select_country(self, country_value):

        country_dropdown = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.View").instance(21)',
        )

        country_dropdown.click()

        time.sleep(0.25)

        search_country = self.driver.find_element(
            AppiumBy.CLASS_NAME, "android.widget.EditText"
        )

        search_country.click()

        search_country.send_keys(country_value)

        time.sleep(0.25)

        country = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, country_value)

        country.click()

        time.sleep(0.25)

    def save_vendor(self):

        print("[UI] Clicked on Save button")

        save_button = self.driver.find_element(*self.SAVE_BUTTON)

        save_button.click()

        time.sleep(3)

    def upload_document(self):

        print("[UI] Uploading document")

        documents_tab = self.driver.find_element(
            AppiumBy.XPATH, '//*[contains(@content-desc,"Documents")]'
        )

        documents_tab.click()

        time.sleep(0.25)

        upload_files = self.driver.find_element(*self.UPLOAD_FILES)

        upload_files.click()

        time.sleep(0.5)

        file_select = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.google.android.documentsui:id/icon_thumb").instance(0)',
        )

        file_select.click()

        time.sleep(3)
