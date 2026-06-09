import time
import allure

from appium.webdriver.common.appiumby import AppiumBy


class ExpensesPage:

    def __init__(self, driver):
        self.driver = driver

    def open_expenses(self):

        with allure.step("Open Expenses section"):

            print("[UI] Looking for Expenses menu")

            expenses_menu = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                "new UiScrollable(new UiSelector().scrollable(true))"
                '.scrollIntoView(new UiSelector().description("Expenses"))',
            )

            expenses_menu.click()

    def click_new_expense(self):

        with allure.step("Click New Expense"):

            print("[UI] Looking for New Expense button")

            new_expense = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "New Expense",
            )

            new_expense.click()
            time.sleep(2)

    def select_customer(self, customer_name):

        with allure.step("Select Customer"):

            print("[UI] Looking for Customer dropdown")

            customer_dropdown = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(19)',
            )

            customer_dropdown.click()
            time.sleep(1)

            customer = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                customer_name,
            )

            customer.click()
            time.sleep(2)

    def select_project(self, project_name):

        with allure.step("Select Project"):

            print("[UI] Looking for Project dropdown")

            project_dropdown = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(20)',
            )

            project_dropdown.click()
            time.sleep(1)

            project = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                project_name,
            )

            project.click()
            time.sleep(2)

    def select_expense_type(self, expense_type):

        with allure.step("Select Expense Type"):

            print("[UI] Looking for Expense Type dropdown")

            expense_type_dropdown = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(21)',
            )

            expense_type_dropdown.click()
            time.sleep(1)

            expense_type_element = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().description("{expense_type}").instance(0)',
            )

            expense_type_element.click()
            time.sleep(2)

    def select_category(self, category):

        with allure.step("Select Category"):

            print("[UI] Looking for Category dropdown")

            category_dropdown = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(22)',
            )

            category_dropdown.click()
            time.sleep(1)

            category_element = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                category,
            )

            category_element.click()
            time.sleep(2)

    def select_user(self):

        with allure.step("Select User"):

            print("[UI] Looking for User dropdown")

            user_dropdown = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "User",
            )

            user_dropdown.click()
            time.sleep(1)

            new_user = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "New User",
            )

            new_user.click()
            time.sleep(2)

    def enter_amount(self, amount):

        with allure.step("Enter Amount"):

            print("[UI] Looking for Amount field")

            amount_field = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(0)',
            )

            amount_field.click()
            amount_field.clear()
            amount_field.send_keys(str(amount))

            time.sleep(1)

    def open_notes_tab(self):

        with allure.step("Open Notes Tab"):

            print("[UI] Looking for Notes tab")

            notes_tab = self.driver.find_element(
                AppiumBy.XPATH,
                '//android.view.View[@content-desc="Notes\nTab 2 of 3"]',
            )

            notes_tab.click()
            time.sleep(2)

    def enter_notes(self, notes):

        with allure.step("Enter Notes"):

            print("[UI] Looking for Notes field")

            notes_field = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(0)',
            )

            notes_field.click()
            notes_field.send_keys(notes)

            time.sleep(1)

    def enter_vendor_notes(self, vendor_notes):

        with allure.step("Enter Vendor Notes"):

            print("[UI] Looking for Vendor Notes field")

            vendor_notes_field = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(1)',
            )

            vendor_notes_field.click()
            vendor_notes_field.send_keys(vendor_notes)

            time.sleep(1)

    def open_settings_tab(self):

        with allure.step("Open Settings Tab"):

            print("[UI] Looking for Settings tab")

            settings_tab = self.driver.find_element(
                AppiumBy.XPATH,
                '//android.view.View[@content-desc="Settings\nTab 3 of 3"]',
            )

            settings_tab.click()
            time.sleep(2)

    def enable_should_be_invoiced(self):

        with allure.step("Enable Should Be Invoiced"):

            print("[UI] Tapping to enable Should Be Invoiced")

            self.driver.tap([(590, 350)], 500)

            time.sleep(1)

    def enable_add_documents_to_invoice(self):

        with allure.step("Enable Add Documents to Invoice"):

            print("[UI] Tapping to enable Add Documents to Invoice")

            self.driver.tap([(575, 711)], 500)

            time.sleep(1)

    def save(self):

        with allure.step("Save Expense"):

            print("[UI] Looking for Save button")

            save_btn = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "Save",
            )

            save_btn.click()

            time.sleep(5)

    def verify_expense_created(self, customer):

        with allure.step("Verify Expense Created Successfully"):

            print("[UI] Verifying expense creation")

            customer_label = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                customer,
            )

            assert (
                customer_label.is_displayed()
            ), f"Expense creation failed. {customer} not found."

            print(f"[PASS] Expense successfully created for {customer}")
