import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ---------------------------------------------------------
    # Locators
    # ---------------------------------------------------------

    NEW_PRODUCT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "New Product")

    PRODUCT_NAME_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    DESCRIPTION_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    PRICE_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )

    DEFAULT_QUANTITY_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")')

    DEFAULT_QUANTITY_INSTANCE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(3)',
    )

    MAX_QUANTITY_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(4)',
    )

    IMAGE_URL_FIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(5)',
    )

    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Save")

    EDIT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Edit")

    DOCUMENTS_TAB = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Documents\nTab 2 of 2"]',
    )

    UPLOAD_FILES_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Upload Files")

    FILE_SELECT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.google.android.documentsui:id/icon_thumb").instance(0)',
    )

    IMAGE_VIEW = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.ImageView")',
    )

    # ---------------------------------------------------------
    # Actions
    # ---------------------------------------------------------

    def click_new_product(self):

        self.wait.until(EC.presence_of_element_located(self.NEW_PRODUCT_BUTTON)).click()

    def enter_product_name(self, value):

        field = self.driver.find_element(*self.PRODUCT_NAME_FIELD)

        field.send_keys(value)

    def enter_description(self, value):

        field = self.driver.find_element(*self.DESCRIPTION_FIELD)

        field.click()

        time.sleep(0.5)

        field.send_keys(value)

    def enter_price(self, value):

        field = self.driver.find_element(*self.PRICE_FIELD)

        field.click()

        time.sleep(0.5)

        field.send_keys(str(value))

    def enter_default_quantity(self, value):

        try:
            field = self.driver.find_element(*self.DEFAULT_QUANTITY_TEXT)

        except Exception:
            field = self.driver.find_element(*self.DEFAULT_QUANTITY_INSTANCE)

        field.click()

        time.sleep(0.5)

        field.clear()

        time.sleep(0.5)

        try:
            field = self.driver.find_element(*self.DEFAULT_QUANTITY_INSTANCE)

            field.click()

        except Exception:
            field = self.driver.find_element(*self.DEFAULT_QUANTITY_TEXT)

            field.click()

        field.send_keys(str(value))

    def enter_max_quantity(self, value):

        field = self.driver.find_element(*self.MAX_QUANTITY_FIELD)

        field.click()

        time.sleep(0.5)

        field.send_keys(str(value))

    def enter_image_url(self, value):

        field = self.driver.find_element(*self.IMAGE_URL_FIELD)

        field.click()

        time.sleep(0.5)

        field.send_keys(value)

    def click_save(self):

        save_btn = self.driver.find_element(*self.SAVE_BUTTON)

        save_btn.click()

        time.sleep(1.5)

    def verify_edit_displayed(self):

        edit_btn = self.wait.until(EC.presence_of_element_located(self.EDIT_BUTTON))

        assert edit_btn.is_displayed()

    def open_documents_tab(self):

        documents_tab = self.driver.find_element(*self.DOCUMENTS_TAB)

        documents_tab.click()

    def click_upload_files(self):

        upload_btn = self.wait.until(
            EC.presence_of_element_located(self.UPLOAD_FILES_BUTTON)
        )

        upload_btn.click()

    def select_file(self):

        file_element = self.wait.until(EC.presence_of_element_located(self.FILE_SELECT))

        file_element.click()

        time.sleep(1.5)

    def verify_image_uploaded(self):

        image = self.wait.until(EC.presence_of_element_located(self.IMAGE_VIEW))

        assert image.is_displayed()
