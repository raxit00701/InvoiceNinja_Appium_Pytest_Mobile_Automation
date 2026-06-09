import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


class ProjectsPage:
    def __init__(self, driver):
        self.driver = driver

    # ================= LOCATORS =================

    PROJECTS_MENU = (AppiumBy.ACCESSIBILITY_ID, "Projects")

    NEW_PROJECT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "New Project")

    PROJECT_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    COMPANY_DROPDOWN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(12)',
    )

    USER_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "User")

    DATE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    AMOUNT_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    TAX_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    DESCRIPTION_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(4)',
    )

    NOTES_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(5)',
    )

    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Save")

    INVOICE_PROJECT = (AppiumBy.ACCESSIBILITY_ID, "Invoice Project")

    # ================= ACTION METHODS =================

    def open_projects_section(self):

        print("[UI] Looking for Projects menu")

        projects = self.driver.find_element(*self.PROJECTS_MENU)

        assert projects.is_displayed(), "Projects menu not visible"

        print("[UI] Clicking Projects")

        projects.click()

        time.sleep(0.5)

    def click_new_project(self):

        print("[UI] Looking for New Project button")

        new_project = self.driver.find_element(*self.NEW_PROJECT_BUTTON)

        assert new_project.is_displayed(), "New Project button not visible"

        print("[UI] Clicking New Project")

        new_project.click()

        time.sleep(0.5)

    def enter_project_name(self, project_name):

        print("[UI] Entering Project Name")

        field = self.driver.find_element(*self.PROJECT_NAME_FIELD)

        field.click()
        field.send_keys(project_name)

        time.sleep(0.5)

    def select_company(self, company_name):

        print("[UI] Opening Company dropdown")

        dropdown = self.driver.find_element(*self.COMPANY_DROPDOWN)

        dropdown.click()

        time.sleep(0.5)

        print("[UI] Selecting Company")

        company = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, company_name)

        company.click()

        time.sleep(0.5)

    def select_user(self, user_name):

        print("[UI] Opening User dropdown")

        dropdown = self.driver.find_element(*self.USER_DROPDOWN)

        dropdown.click()

        time.sleep(0.5)

        print("[UI] Selecting User")

        user = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, user_name)

        user.click()

        time.sleep(0.5)

    def enter_date(self, date):

        print("[UI] Entering Date")

        field = self.driver.find_element(*self.DATE_FIELD)

        field.click()
        field.send_keys(date)

        time.sleep(0.5)

    def enter_amount(self, amount):

        print("[UI] Entering Amount")

        field = self.driver.find_element(*self.AMOUNT_FIELD)

        field.click()
        field.send_keys(str(amount))

        time.sleep(0.5)

    def enter_tax(self, tax):

        print("[UI] Entering Tax")

        field = self.driver.find_element(*self.TAX_FIELD)

        field.click()
        field.send_keys(tax)

        time.sleep(0.5)

    def enter_description(self, description):

        print("[UI] Entering Description")

        field = self.driver.find_element(*self.DESCRIPTION_FIELD)

        field.click()
        field.send_keys(description)

        time.sleep(0.5)

    def enter_notes(self, notes):

        print("[UI] Entering Notes")

        field = self.driver.find_element(*self.NOTES_FIELD)

        field.click()
        field.send_keys(notes)

        time.sleep(0.5)

    def click_save(self):

        print("[UI] Clicking Save button")

        save_button = self.driver.find_element(*self.SAVE_BUTTON)

        assert save_button.is_displayed(), "Save button not visible"

        save_button.click()

        time.sleep(2)

    def verify_invoice_project(self):

        print("[UI] Looking for 'Invoice Project' accessibility ID")

        invoice_project = self.driver.find_element(*self.INVOICE_PROJECT)

        assert (
            invoice_project.is_displayed()
        ), "'Invoice Project' accessibility ID not visible"

        print(f"[UI] Found 'Invoice Project' element with text: {invoice_project.text}")

        time.sleep(0.5)
