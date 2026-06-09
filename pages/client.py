import time
import allure

from appium.webdriver.common.appiumby import AppiumBy


class ClientPage:
    def __init__(self, driver):
        self.driver = driver

    # ==============================
    # LOCATORS
    # ==============================

    CLIENT_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    USER_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "User")

    NEW_USER_OPTION = (AppiumBy.ACCESSIBILITY_ID, "New User")

    ID_NUMBER_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    VAT_NUMBER_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    WEBSITE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    PHONE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(4)',
    )

    CONTACTS_TAB = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Contacts\nTab 2 of 6")',
    )

    FIRST_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    LAST_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    EMAIL_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    CONTACT_PHONE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    # ==============================
    # ACTION METHODS
    # ==============================

    def enter_client_name(self, client_name):

        with allure.step("Enter client name"):
            print(f"[UI] Entering Client Name: {client_name}")

            name_field = self.driver.find_element(*self.CLIENT_NAME_FIELD)

            assert name_field.is_displayed(), "Client name field not visible"

            name_field.click()
            name_field.clear()
            name_field.send_keys(client_name)

            print("[UI] Client name entered successfully")

            time.sleep(0.5)

    def select_new_user(self):

        with allure.step("Select New User from dropdown"):
            print("[UI] Opening User dropdown")

            user_dropdown = self.driver.find_element(*self.USER_DROPDOWN)

            assert user_dropdown.is_displayed(), "User dropdown not visible"

            user_dropdown.click()

            time.sleep(0.5)

            print("[UI] Looking for New User option")

            new_user = self.driver.find_element(*self.NEW_USER_OPTION)

            assert new_user.is_displayed(), "New User option not visible"

            print("[UI] Selecting New User")

            new_user.click()

            time.sleep(0.5)

    def enter_id_number(self, id_number):

        with allure.step("Enter ID number"):
            print(f"[UI] Entering ID Number: {id_number}")

            id_field = self.driver.find_element(*self.ID_NUMBER_FIELD)

            assert id_field.is_displayed(), "ID number field not visible"

            id_field.click()
            id_field.clear()
            id_field.send_keys(id_number)

            print("[UI] ID Number entered successfully")

            time.sleep(0.5)

    def enter_vat_number(self, vat_number):

        with allure.step("Enter VAT number"):
            print(f"[UI] Entering VAT Number: {vat_number}")

            vat_field = self.driver.find_element(*self.VAT_NUMBER_FIELD)

            assert vat_field.is_displayed(), "VAT number field not visible"

            vat_field.click()
            vat_field.clear()
            vat_field.send_keys(vat_number)

            print("[UI] VAT Number entered successfully")

            time.sleep(0.5)

    def enter_website(self, website):

        with allure.step("Enter website"):
            print(f"[UI] Entering Website: {website}")

            website_field = self.driver.find_element(*self.WEBSITE_FIELD)

            assert website_field.is_displayed(), "Website field not visible"

            website_field.click()
            website_field.clear()
            website_field.send_keys(website)

            print("[UI] Website entered successfully")

            time.sleep(0.5)

    def enter_phone_number(self, phone):

        with allure.step("Enter phone number"):
            print(f"[UI] Entering Phone Number: {phone}")

            phone_field = self.driver.find_element(*self.PHONE_FIELD)

            assert phone_field.is_displayed(), "Phone number field not visible"

            phone_field.click()
            phone_field.clear()
            phone_field.send_keys(phone)

            print("[UI] Phone Number entered successfully")

            time.sleep(0.5)

    # ==============================
    # CONTACTS TAB METHODS
    # ==============================

    def navigate_to_contacts_tab(self):

        with allure.step("Navigate to Contacts Tab"):
            print("[UI] Clicking Contacts Tab (Tab 2 of 6)")

            contacts_tab = self.driver.find_element(*self.CONTACTS_TAB)

            assert contacts_tab.is_displayed(), "Contacts Tab not visible"

            contacts_tab.click()

            time.sleep(0.5)

    def enter_first_name(self, first_name):

        with allure.step("Enter contact first name"):
            print(f"[UI] Entering First Name: {first_name}")

            first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)

            assert first_name_field.is_displayed(), "First name field not visible"

            first_name_field.click()
            first_name_field.clear()
            first_name_field.send_keys(first_name)

            print("[UI] First name entered successfully")

            time.sleep(0.5)

    def enter_last_name(self, last_name):

        with allure.step("Enter contact last name"):
            print(f"[UI] Entering Last Name: {last_name}")

            last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)

            assert last_name_field.is_displayed(), "Last name field not visible"

            last_name_field.click()
            last_name_field.clear()
            last_name_field.send_keys(last_name)

            print("[UI] Last name entered successfully")

            time.sleep(0.5)

    def enter_contact_email(self, email):

        with allure.step("Enter contact email"):
            print(f"[UI] Entering Email: {email}")

            email_field = self.driver.find_element(*self.EMAIL_FIELD)

            assert email_field.is_displayed(), "Email field not visible"

            email_field.click()
            email_field.clear()
            email_field.send_keys(email)

            print("[UI] Email entered successfully")

            time.sleep(0.5)

    def enter_contact_phone(self, phone):

        with allure.step("Enter contact phone"):
            print(f"[UI] Entering Contact Phone: {phone}")

            contact_phone_field = self.driver.find_element(*self.CONTACT_PHONE_FIELD)

            assert contact_phone_field.is_displayed(), "Contact phone field not visible"

            contact_phone_field.click()
            contact_phone_field.clear()
            contact_phone_field.send_keys(phone)

            print("[UI] Contact phone entered successfully")

            time.sleep(0.5)
        # ==============================

    # SECOND CONTACT LOCATORS
    # ==============================

    ADD_SECOND_CONTACT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("ADD SECOND CONTACT")',
    )

    SECOND_CONTACT_FIRST_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    SECOND_CONTACT_LAST_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    SECOND_CONTACT_EMAIL_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    SECOND_CONTACT_PHONE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    DONE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "DONE")

    # ==============================
    # SECOND CONTACT METHODS
    # ==============================

    def click_add_second_contact(self):

        with allure.step("Add second contact"):
            print("[UI] Clicking ADD SECOND CONTACT")

            add_second_contact = self.driver.find_element(
                *self.ADD_SECOND_CONTACT_BUTTON
            )

            assert (
                add_second_contact.is_displayed()
            ), "ADD SECOND CONTACT button not visible"

            add_second_contact.click()

            print("[UI] Waiting for second contact popup to open")

            time.sleep(0.5)

    def enter_second_contact_first_name(self, first_name):

        with allure.step("Enter second contact first name"):
            print(f"[UI] Entering Second Contact First Name: {first_name}")

            second_first_name_field = self.driver.find_element(
                *self.SECOND_CONTACT_FIRST_NAME_FIELD
            )

            assert (
                second_first_name_field.is_displayed()
            ), "Second contact first name field not visible"

            second_first_name_field.click()
            second_first_name_field.clear()
            second_first_name_field.send_keys(first_name)

            print("[UI] Second contact first name entered successfully")

            time.sleep(0.5)

    def enter_second_contact_last_name(self, last_name):

        with allure.step("Enter second contact last name"):
            print(f"[UI] Entering Second Contact Last Name: {last_name}")

            second_last_name_field = self.driver.find_element(
                *self.SECOND_CONTACT_LAST_NAME_FIELD
            )

            assert (
                second_last_name_field.is_displayed()
            ), "Second contact last name field not visible"

            second_last_name_field.click()
            second_last_name_field.clear()
            second_last_name_field.send_keys(last_name)

            print("[UI] Second contact last name entered successfully")

            time.sleep(0.5)

    def enter_second_contact_email(self, email):

        with allure.step("Enter second contact email"):
            print(f"[UI] Entering Second Contact Email: {email}")

            second_email_field = self.driver.find_element(
                *self.SECOND_CONTACT_EMAIL_FIELD
            )

            assert (
                second_email_field.is_displayed()
            ), "Second contact email field not visible"

            second_email_field.click()
            second_email_field.clear()
            second_email_field.send_keys(email)

            print("[UI] Second contact email entered successfully")

            time.sleep(0.5)

    def enter_second_contact_phone(self, phone):

        with allure.step("Enter second contact phone"):
            print(f"[UI] Entering Second Contact Phone: {phone}")

            second_phone_field = self.driver.find_element(
                *self.SECOND_CONTACT_PHONE_FIELD
            )

            assert (
                second_phone_field.is_displayed()
            ), "Second contact phone field not visible"

            second_phone_field.click()
            second_phone_field.clear()
            second_phone_field.send_keys(phone)

            print("[UI] Second contact phone entered successfully")

            time.sleep(0.5)

    def click_done_button(self):

        with allure.step("Confirm second contact with DONE"):
            print("[UI] Clicking DONE to confirm second contact")

            done_button = self.driver.find_element(*self.DONE_BUTTON)

            assert done_button.is_displayed(), "DONE button not visible"

            done_button.click()

            time.sleep(0.5)

    # ==============================
    # NOTES TAB LOCATORS
    # ==============================

    NOTES_TAB = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Notes\nTab 3 of 6")',
    )

    PUBLIC_NOTES_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    PRIVATE_NOTES_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    # ==============================
    # NOTES TAB METHODS
    # ==============================

    def navigate_to_notes_tab(self):

        with allure.step("Navigate to Notes Tab"):
            print("[UI] Clicking Notes Tab (Tab 3 of 6)")

            notes_tab = self.driver.find_element(*self.NOTES_TAB)

            assert notes_tab.is_displayed(), "Notes Tab not visible"

            notes_tab.click()

            time.sleep(0.5)

    def enter_public_notes(self, public_notes):

        with allure.step("Enter public notes"):
            print(f"[UI] Entering Public Notes: {public_notes}")

            public_notes_field = self.driver.find_element(*self.PUBLIC_NOTES_FIELD)

            assert public_notes_field.is_displayed(), "Public notes field not visible"

            public_notes_field.click()
            public_notes_field.clear()
            public_notes_field.send_keys(public_notes)

            print("[UI] Public notes entered successfully")

    def enter_private_notes(self, private_notes):

        with allure.step("Enter private notes"):
            print(f"[UI] Entering Private Notes: {private_notes}")

            private_notes_field = self.driver.find_element(*self.PRIVATE_NOTES_FIELD)

            assert private_notes_field.is_displayed(), "Private notes field not visible"

            private_notes_field.click()
            private_notes_field.clear()
            private_notes_field.send_keys(private_notes)

            print("[UI] Private notes entered successfully")

            time.sleep(0.5)

    # ==============================
    # SETTINGS TAB LOCATORS
    # ==============================

    SETTINGS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Settings\nTab 4 of 6"]',
    )

    LANGUAGE_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(22)',
    )

    PAYMENT_TERMS_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "Invoice Payment Terms")

    QUOTE_VALID_UNTIL_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "Quote Valid Until")

    SEND_REMINDERS_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "Send Reminders")

    CUSTOM_VALUE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText")',
    )

    SIZE_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "Size")

    # ==============================
    # SETTINGS TAB METHODS
    # ==============================

    def navigate_to_settings_tab(self):

        with allure.step("Navigate to Settings Tab"):
            print("[UI] Clicking Settings Tab (Tab 4 of 6)")

            settings_tab = self.driver.find_element(*self.SETTINGS_TAB)

            assert settings_tab.is_displayed(), "Settings Tab not visible"

            settings_tab.click()

            time.sleep(0.5)

    def select_language(self, language):

        with allure.step("Select language"):
            print(f"[UI] Opening Language dropdown")

            language_dropdown = self.driver.find_element(*self.LANGUAGE_DROPDOWN)

            assert language_dropdown.is_displayed(), "Language dropdown not visible"

            language_dropdown.click()

            time.sleep(0.5)

            print(f"[UI] Scrolling to find language: {language}")

            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f"new UiScrollable(new UiSelector().scrollable(true))"
                f".scrollIntoView("
                f"new UiSelector().description("
                f'"{language}"))',
            )

            language_option = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().description("{language}")',
            )

            assert (
                language_option.is_displayed()
            ), f"Language option '{language}' not visible"

            language_option.click()

            print(f"[UI] Language '{language}' selected")

            time.sleep(0.5)

    def select_invoice_payment_terms(self, payment_term):

        with allure.step("Select Invoice Payment Terms"):
            print("[UI] Opening Invoice Payment Terms dropdown")

            payment_terms_dropdown = self.driver.find_element(
                *self.PAYMENT_TERMS_DROPDOWN
            )

            assert (
                payment_terms_dropdown.is_displayed()
            ), "Invoice Payment Terms dropdown not visible"

            payment_terms_dropdown.click()

            time.sleep(0.5)

            payment_term_option = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, payment_term
            )

            assert (
                payment_term_option.is_displayed()
            ), f"Payment term '{payment_term}' not visible"

            payment_term_option.click()

            print(f"[UI] Invoice Payment Terms set to '{payment_term}'")

            time.sleep(0.5)

    def select_quote_valid_until(self, quote_valid_until):

        with allure.step("Select Quote Valid Until"):
            print("[UI] Opening Quote Valid Until dropdown")

            quote_valid_dropdown = self.driver.find_element(
                *self.QUOTE_VALID_UNTIL_DROPDOWN
            )

            assert (
                quote_valid_dropdown.is_displayed()
            ), "Quote Valid Until dropdown not visible"

            quote_valid_dropdown.click()

            time.sleep(0.5)

            quote_valid_option = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, quote_valid_until
            )

            assert (
                quote_valid_option.is_displayed()
            ), f"Quote Valid Until option '{quote_valid_until}' not visible"

            quote_valid_option.click()

            print(f"[UI] Quote Valid Until set to '{quote_valid_until}'")

            time.sleep(0.5)

    def select_send_reminders(self, reminders_option_text):

        with allure.step("Select Send Reminders setting"):
            print("[UI] Opening Send Reminders dropdown")

            send_reminders_dropdown = self.driver.find_element(
                *self.SEND_REMINDERS_DROPDOWN
            )

            assert (
                send_reminders_dropdown.is_displayed()
            ), "Send Reminders dropdown not visible"

            send_reminders_dropdown.click()

            time.sleep(0.5)

            reminders_option = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, reminders_option_text
            )

            assert (
                reminders_option.is_displayed()
            ), f"Send Reminders option '{reminders_option_text}' not visible"

            reminders_option.click()

            print(f"[UI] Send Reminders set to '{reminders_option_text}'")

            time.sleep(0.5)

    def enter_custom_value(self, custom_value):

        with allure.step("Enter custom value"):
            print(f"[UI] Entering Custom Value: {custom_value}")

            custom_value_field = self.driver.find_element(*self.CUSTOM_VALUE_FIELD)

            assert custom_value_field.is_displayed(), "Custom value field not visible"

            custom_value_field.click()
            custom_value_field.clear()
            custom_value_field.send_keys(custom_value)

            print("[UI] Custom value entered successfully")

            time.sleep(0.5)

    def select_size(self, size):

        with allure.step("Select client size"):
            print(f"[UI] Opening Size dropdown")

            size_dropdown = self.driver.find_element(*self.SIZE_DROPDOWN)

            assert size_dropdown.is_displayed(), "Size dropdown not visible"

            size_dropdown.click()

            time.sleep(0.5)

            size_option = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, size)

            assert size_option.is_displayed(), f"Size option '{size}' not visible"

            size_option.click()

            print(f"[UI] Size set to '{size}'")

            time.sleep(0.5)

    # ==============================
    # BILLING ADDRESS TAB LOCATORS
    # ==============================

    BILLING_ADDRESS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Billing Address\nTab 5 of 6"]',
    )

    BILLING_STREET_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    BILLING_APT_SUITE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    BILLING_CITY_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    BILLING_STATE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    BILLING_POSTAL_CODE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(4)',
    )

    BILLING_COUNTRY_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(20)',
    )

    BILLING_COUNTRY_SEARCH_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText")',
    )

    # ==============================
    # BILLING ADDRESS TAB METHODS
    # ==============================

    def navigate_to_billing_address_tab(self):

        with allure.step("Navigate to Billing Address Tab"):
            print("[UI] Clicking Billing Address Tab (Tab 5 of 6)")

            billing_tab = self.driver.find_element(*self.BILLING_ADDRESS_TAB)

            assert billing_tab.is_displayed(), "Billing Address Tab not visible"

            billing_tab.click()

            time.sleep(0.5)

    def enter_billing_street(self, street):

        with allure.step("Enter billing street"):
            print(f"[UI] Entering Billing Street: {street}")

            billing_street = self.driver.find_element(*self.BILLING_STREET_FIELD)

            assert billing_street.is_displayed(), "Billing street field not visible"

            billing_street.click()
            billing_street.clear()
            billing_street.send_keys(street)

            time.sleep(0.5)

    def enter_billing_apt_suite(self, apt_suite):

        with allure.step("Enter billing apt/suite"):
            print(f"[UI] Entering Billing Apt/Suite: {apt_suite}")

            billing_apt = self.driver.find_element(*self.BILLING_APT_SUITE_FIELD)

            assert billing_apt.is_displayed(), "Billing apt/suite field not visible"

            billing_apt.click()
            billing_apt.clear()
            billing_apt.send_keys(apt_suite)

            time.sleep(0.5)

    def enter_billing_city(self, city):

        with allure.step("Enter billing city"):
            print(f"[UI] Entering Billing City: {city}")

            billing_city = self.driver.find_element(*self.BILLING_CITY_FIELD)

            assert billing_city.is_displayed(), "Billing city field not visible"

            billing_city.click()
            billing_city.clear()
            billing_city.send_keys(city)

            time.sleep(0.5)

    def enter_billing_state(self, state):

        with allure.step("Enter billing state"):
            print(f"[UI] Entering Billing State: {state}")

            billing_state = self.driver.find_element(*self.BILLING_STATE_FIELD)

            assert billing_state.is_displayed(), "Billing state field not visible"

            billing_state.click()
            billing_state.clear()
            billing_state.send_keys(state)

            time.sleep(0.5)

    def enter_billing_postal_code(self, postal_code):

        with allure.step("Enter billing postal code"):
            print(f"[UI] Entering Billing Postal Code: {postal_code}")

            billing_postal = self.driver.find_element(*self.BILLING_POSTAL_CODE_FIELD)

            assert (
                billing_postal.is_displayed()
            ), "Billing postal code field not visible"

            billing_postal.click()
            billing_postal.clear()
            billing_postal.send_keys(postal_code)

            time.sleep(0.5)

    def select_billing_country(self, country_search, country):

        with allure.step("Select billing country"):
            print("[UI] Opening Billing Country dropdown")

            billing_country_dropdown = self.driver.find_element(
                *self.BILLING_COUNTRY_DROPDOWN
            )

            assert (
                billing_country_dropdown.is_displayed()
            ), "Billing country dropdown not visible"

            billing_country_dropdown.click()

            time.sleep(0.5)

            billing_country_search = self.driver.find_element(
                *self.BILLING_COUNTRY_SEARCH_FIELD
            )

            billing_country_search.send_keys(country_search)

            time.sleep(0.5)

            billing_country_option = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, country
            )

            assert (
                billing_country_option.is_displayed()
            ), f"Billing country '{country}' not visible"

            billing_country_option.click()

            print(f"[UI] Billing country set to '{country}'")

            time.sleep(0.5)

    # ==============================
    # SHIPPING ADDRESS TAB LOCATORS
    # ==============================

    SHIPPING_ADDRESS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Shipping Address\nTab 6 of 6"]',
    )

    SHIPPING_STREET_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    SHIPPING_APT_SUITE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    SHIPPING_CITY_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    SHIPPING_STATE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    SHIPPING_POSTAL_CODE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(4)',
    )

    SHIPPING_COUNTRY_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(20)',
    )

    SHIPPING_COUNTRY_SEARCH_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText")',
    )

    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Save")

    # ==============================
    # SHIPPING ADDRESS TAB METHODS
    # ==============================

    def navigate_to_shipping_address_tab(self):

        with allure.step("Navigate to Shipping Address Tab"):
            print("[UI] Clicking Shipping Address Tab (Tab 6 of 6)")

            shipping_tab = self.driver.find_element(*self.SHIPPING_ADDRESS_TAB)

            assert shipping_tab.is_displayed(), "Shipping Address Tab not visible"

            shipping_tab.click()

            time.sleep(0.5)

    def enter_shipping_street(self, street):

        with allure.step("Enter shipping street"):
            print(f"[UI] Entering Shipping Street: {street}")

            shipping_street = self.driver.find_element(*self.SHIPPING_STREET_FIELD)

            assert shipping_street.is_displayed(), "Shipping street field not visible"

            shipping_street.click()
            shipping_street.clear()
            shipping_street.send_keys(street)

            time.sleep(0.5)

    def enter_shipping_apt_suite(self, apt_suite):

        with allure.step("Enter shipping apt/suite"):
            print(f"[UI] Entering Shipping Apt/Suite: {apt_suite}")

            shipping_apt = self.driver.find_element(*self.SHIPPING_APT_SUITE_FIELD)

            assert shipping_apt.is_displayed(), "Shipping apt/suite field not visible"

            shipping_apt.click()
            shipping_apt.clear()
            shipping_apt.send_keys(apt_suite)

            time.sleep(0.5)

    def enter_shipping_city(self, city):

        with allure.step("Enter shipping city"):
            print(f"[UI] Entering Shipping City: {city}")

            shipping_city = self.driver.find_element(*self.SHIPPING_CITY_FIELD)

            assert shipping_city.is_displayed(), "Shipping city field not visible"

            shipping_city.click()
            shipping_city.clear()
            shipping_city.send_keys(city)

            time.sleep(0.5)

    def enter_shipping_state(self, state):

        with allure.step("Enter shipping state"):
            print(f"[UI] Entering Shipping State: {state}")

            shipping_state = self.driver.find_element(*self.SHIPPING_STATE_FIELD)

            assert shipping_state.is_displayed(), "Shipping state field not visible"

            shipping_state.click()
            shipping_state.clear()
            shipping_state.send_keys(state)

            time.sleep(0.5)

    def enter_shipping_postal_code(self, postal_code):

        with allure.step("Enter shipping postal code"):
            print(f"[UI] Entering Shipping Postal Code: {postal_code}")

            shipping_postal = self.driver.find_element(*self.SHIPPING_POSTAL_CODE_FIELD)

            assert (
                shipping_postal.is_displayed()
            ), "Shipping postal code field not visible"

            shipping_postal.click()
            shipping_postal.clear()
            shipping_postal.send_keys(postal_code)

            time.sleep(0.5)

    def select_shipping_country(self, country_search, country):

        with allure.step("Select shipping country"):
            print("[UI] Opening Shipping Country dropdown")

            shipping_country_dropdown = self.driver.find_element(
                *self.SHIPPING_COUNTRY_DROPDOWN
            )

            assert (
                shipping_country_dropdown.is_displayed()
            ), "Shipping country dropdown not visible"

            shipping_country_dropdown.click()

            time.sleep(0.5)

            shipping_country_search = self.driver.find_element(
                *self.SHIPPING_COUNTRY_SEARCH_FIELD
            )

            shipping_country_search.send_keys(country_search)

            time.sleep(0.5)

            shipping_country_option = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, country
            )

            assert (
                shipping_country_option.is_displayed()
            ), f"Shipping country '{country}' not visible"

            shipping_country_option.click()

            print(f"[UI] Shipping country set to '{country}'")

            time.sleep(0.5)

    def click_save_button(self):

        with allure.step("Save client"):
            print("[UI] Looking for Save button")

            save_button = self.driver.find_element(*self.SAVE_BUTTON)

            assert save_button.is_displayed(), "Save button not visible"

            print("[UI] Clicking Save")

            save_button.click()

            print("[UI] Waiting for save operation to complete")

            time.sleep(2)
