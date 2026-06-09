import time

import allure
from appium.webdriver.common.appiumby import AppiumBy


class QuotesPage:

    def __init__(self, driver):
        self.driver = driver

    # Step 3 - Click New Quote
    def click_new_quote(self):

        with allure.step("Click New Quote"):

            print("[UI] Clicking New Quote")

            el4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "New Quote")

            el4.click()

            time.sleep(1)

    # Step 4 - Select Company Dropdown
    def open_company_dropdown(self):

        with allure.step("Select company dropdown"):

            print("[UI] Opening Company Dropdown")

            el5 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(22)',
            )

            el5.click()

            time.sleep(1)

    # Step 5 - Select Company
    def select_company(self, company):

        with allure.step("Select Company"):

            print(f"[UI] Selecting Company : {company}")

            el6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, company)

            el6.click()

            time.sleep(1)

    # Step 6 - Open User Dropdown
    def open_user_dropdown(self):

        with allure.step("Open User Dropdown"):

            print("[UI] Clicking User Dropdown")

            el7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "User")

            el7.click()

            time.sleep(1)

    # Step 7 - Select User
    def select_user(self, user):

        with allure.step("Select User"):

            print(f"[UI] Selecting User : {user}")

            el8 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, user)

            el8.click()

            time.sleep(1)

    # Step 8 - Enter Quote Date
    def enter_quote_date(self, quote_date):

        with allure.step("Enter Quote Date"):

            print(f"[UI] Entering Quote Date : {quote_date}")

            el9 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(1)',
            )

            el9.click()

            el9.clear()

            el9.send_keys(quote_date)

            time.sleep(1)

    # Step 9 - Enter PO Number
    def enter_po_number(self, unique_po):

        with allure.step("Enter PO Number"):

            print(f"[UI] Entering Unique PO Number : {unique_po}")

            el10 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(3)',
            )

            el10.click()

            el10.clear()

            el10.send_keys(unique_po)

            time.sleep(1)

    # Step 11 - Enter Quantity
    def enter_quantity(self, quantity):

        with allure.step("Enter Quantity"):

            print(f"[UI] Entering Quantity : {quantity}")

            el11 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(4)',
            )

            el11.click()

            el11.clear()

            el11.send_keys(str(quantity))

            time.sleep(1)

    # Step 10 - Fast Scroll Down
    def scroll_down_quickly(self):

        with allure.step("Scroll Down Quickly"):

            print("[UI] Finger moving UP - Page moving DOWN")

            for i in range(3):

                self.driver.swipe(
                    start_x=282, start_y=1113, end_x=360, end_y=463, duration=300
                )

                time.sleep(0.5)

    # Step 12 - Select Department
    def select_department(self, department):

        with allure.step("Select Department"):

            print(f"[UI] Selecting Department : {department}")

            el12 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, department)

            el12.click()

            time.sleep(1)

    # Step 13 - Select Category
    def select_category(self, category):

        with allure.step("Select Category"):

            print(f"[UI] Selecting Category : {category}")

            el13 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, category)

            el13.click()

            time.sleep(1)

    # Step 14 - Open Dropdown
    def open_logistics_dropdown(self):

        with allure.step("Open Logistics Dropdown"):

            print("[UI] Opening Logistics Dropdown using coordinates")

            self.driver.tap([(360, 804.5)], 500)

            time.sleep(1)

    # Step 15 - Select Test Option
    def select_test_option(self):

        with allure.step("Select Test Option"):

            print("[UI] Selecting Test Option")

            el15 = self.driver.find_element(
                AppiumBy.XPATH,
                '(//android.widget.Button[@content-desc="test"])[1]',
            )

            el15.click()

            time.sleep(1)

    # Step 16 - Open Logistics List
    def open_logistics_list(self):

        with allure.step("Open Logistics List"):

            print("[UI] Opening Logistics List")

            el16 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(23)',
            )

            el16.click()

            time.sleep(1)

    # Step 17 - Select Logistics Company
    def select_logistics_company(self, logistics_company):

        with allure.step("Select Logistics Company"):

            print(f"[UI] Selecting Logistics Company : {logistics_company}")

            el17 = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, logistics_company
            )

            el17.click()

            time.sleep(1)

    # Step 18 - Quantity Edit
    def edit_item_quantity(self, item_quantity):

        with allure.step("Edit Quantity"):

            print("[UI] Editing Quantity")

            el20 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'
            )

            el20.click()

            el20.clear()

            time.sleep(0.5)

            el20 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(4)',
            )

            el20.send_keys(str(item_quantity))

            time.sleep(1)

    # Step 19 - Open Contacts Tab
    def open_contacts_tab(self):

        with allure.step("Open Contacts Tab"):

            print("[UI] Opening Contacts Tab")

            el21 = self.driver.find_element(
                AppiumBy.XPATH,
                '//android.view.View[@content-desc="Contacts\nTab 2 of 5"]',
            )

            el21.click()

            time.sleep(1)

    # Step 20 - Open Items Tab
    def open_items_tab(self):

        with allure.step("Open Items Tab"):

            print("[UI] Opening Items Tab")

            el22 = self.driver.find_element(
                AppiumBy.XPATH, '//android.view.View[@content-desc="Items\nTab 3 of 5"]'
            )

            el22.click()

            time.sleep(1)

    # Step 21 - Add Item
    def click_add_item(self):

        with allure.step("Add Item"):

            print("[UI] Clicking Add Item")

            el23 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add Item")

            el23.click()

            time.sleep(1)

    # Step 22 - Select Product
    def select_product(self):

        with allure.step("Select Product"):

            print("[UI] Selecting Product")

            el24 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().description("Gaming Mouse X200  📎\n$1,299.00\nHigh precision gaming mouse for automation and performance testing").instance(0)',
            )

            assert el24.is_displayed(), "Product not visible"

            print("[UI] Clicking Product")

            el24.click()

            time.sleep(1)

    # Step 23 - Click DONE
    def click_done(self):

        with allure.step("Click DONE"):

            print("[UI] Clicking DONE")

            el25 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "DONE")

            el25.click()

            time.sleep(1)

    # Step 24 - Open Notes Tab
    def open_notes_tab(self):

        with allure.step("Open Notes Tab"):

            print("[UI] Opening Notes Tab")

            el26 = self.driver.find_element(
                AppiumBy.XPATH, '//android.view.View[@content-desc="Notes\nTab 4 of 5"]'
            )

            el26.click()

            time.sleep(1)

    # Step 25 - Enter Note 1
    def enter_note1(self, note1):

        with allure.step("Enter Note 1"):

            print(f"[UI] Entering Note 1 : {note1}")

            el27 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(0)',
            )

            el27.click()

            el27.send_keys(note1)

            time.sleep(0.5)

    # Step 26 - Enter Note 2
    def enter_note2(self, note2):

        with allure.step("Enter Note 2"):

            print(f"[UI] Entering Note 2 : {note2}")

            el28 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(1)',
            )

            el28.click()

            time.sleep(0.5)

            el28.clear()

            time.sleep(0.5)

            el28.send_keys(note2)

            time.sleep(0.5)

            entered_note2 = el28.text

            print(f"[UI NOTE 2 VALUE] {entered_note2}")

            assert note2 in entered_note2, f"""
                UI Note 2 Mismatch
                Expected: {note2}
                Actual: {entered_note2}
            """

            print("[ASSERTION PASSED] Note 2 entered successfully")

    # Step 27 - Enter Note 3
    def enter_note3(self, note3):

        with allure.step("Enter Note 3"):

            print(f"[UI] Entering Note 3 : {note3}")

            el29 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(2)',
            )

            el29.click()

            el29.send_keys(note3)

            time.sleep(0.5)

    # Step 28 - Enter Note 4
    def enter_note4(self, note4):

        with allure.step("Enter Note 4"):

            print(f"[UI] Entering Note 4 : {note4}")

            el30 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(3)',
            )

            el30.click()

            el30.send_keys(note4)

            time.sleep(0.5)

    # Step 29 - Open PDF Tab
    def open_pdf_tab(self):

        with allure.step("Open PDF Tab"):

            print("[UI] Opening PDF Tab")

            el31 = self.driver.find_element(
                AppiumBy.XPATH, '//android.view.View[@content-desc="PDF\nTab 5 of 5"]'
            )

            el31.click()

            time.sleep(8)

    # Step 30 - Verify PDF Preview
    def verify_pdf_preview(self):

        with allure.step("Verify PDF Preview"):

            print("[VERIFY] Checking PDF Preview Visibility")

            el32 = self.driver.find_element(
                AppiumBy.CLASS_NAME, "android.widget.ImageView"
            )

            assert el32.is_displayed(), "PDF Preview not visible"

            print("[VERIFY] PDF Preview Visible")

    # Step 31 - Save Quote
    def click_save(self):

        with allure.step("Save Quote"):

            print("[UI] Clicking Save")

            el33 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Save")

            el33.click()

            time.sleep(2)

    # Step 32 - Verify Quote Saved
    def verify_quote_saved_successfully(self):

        with allure.step("Verify Quote Saved Successfully"):

            print("[VERIFY] Verifying Saved Quote Card")

            el34 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().description("Quote Amount\n$18,510.75\nDraft")',
            )

            assert el34.is_displayed(), "Quote card not visible after save"

            print("[VERIFY] Quote Created Successfully")
