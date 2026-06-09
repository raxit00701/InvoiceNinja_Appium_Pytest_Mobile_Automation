import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SidebarPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ---------------------------------------------------------
    # Locators
    # ---------------------------------------------------------

    CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "CLOSE")

    BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Back")

    MENU_SIDEBAR = (AppiumBy.ACCESSIBILITY_ID, "Menu Sidebar")

    CLIENTS_MENU = (AppiumBy.ACCESSIBILITY_ID, "Clients")

    PRODUCTS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Products")

    PROJECTS_MENU = (AppiumBy.ACCESSIBILITY_ID, "Projects")

    TASKS_MENU = (AppiumBy.ACCESSIBILITY_ID, "Tasks")

    QUOTES_MENU = (AppiumBy.ACCESSIBILITY_ID, "Quotes")

    # ---------------------------------------------------------
    # Actions
    # ---------------------------------------------------------

    def close_initial_popup(self):

        print("[UI] Looking for Close button, Back button, or Menu Sidebar")

        for button in [
            self.CLOSE_BUTTON,
            self.BACK_BUTTON,
            self.MENU_SIDEBAR,
        ]:
            try:

                element = self.driver.find_element(*button)

                if element.is_displayed():

                    print(f"[UI] Clicking element: {button}")

                    element.click()

                    time.sleep(2)

                    # Stop after first visible element is clicked
                    break

            except Exception:
                pass

    def open_sidebar(self):

        print("[UI] Looking for Menu Sidebar")

        sidebar = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.MENU_SIDEBAR)
        )

        assert sidebar.is_displayed(), "Menu Sidebar not visible"

        print("[UI] Clicking Menu Sidebar")

        sidebar.click()

        time.sleep(2)

        print("[UI] Sidebar opened successfully")

    def open_clients(self):

        print("[UI] Looking for Clients menu")

        clients_menu = self.driver.find_element(*self.CLIENTS_MENU)

        assert clients_menu.is_displayed(), "Clients option not visible"

        print("[UI] Clicking Clients")

        clients_menu.click()

        time.sleep(2)

    def click_products(self):

        self.wait.until(EC.presence_of_element_located(self.PRODUCTS_BUTTON)).click()

    def open_projects_section(self):

        print("[UI] Looking for Projects menu")

        projects = self.driver.find_element(*self.PROJECTS_MENU)

        assert projects.is_displayed(), "Projects menu not visible"

        print("[UI] Clicking Projects")

        projects.click()

        time.sleep(2)

        print("[UI] Projects section opened successfully")

    def open_tasks_section(self):

        print("[UI] Looking for Tasks menu")

        tasks_menu = self.driver.find_element(*self.TASKS_MENU)

        assert tasks_menu.is_displayed(), "Tasks menu not visible"

        print("[UI] Clicking Tasks menu")

        tasks_menu.click()

        time.sleep(2)

        print("[UI] Tasks section opened successfully")

    def open_quotes_section(self):

        print("[UI] Looking for Quotes menu")

        quotes_menu = self.driver.find_element(*self.QUOTES_MENU)

        assert quotes_menu.is_displayed(), "Quotes menu not visible"

        print("[UI] Clicking Quotes menu")

        quotes_menu.click()

        time.sleep(2)

        print("[UI] Quotes section opened successfully")

    def click_back_button(self):

        print("[UI] Looking for Back button")

        back_button = self.driver.find_element(
            *self.BACK_BUTTON
        )

        assert back_button.is_displayed(), (
            "Back button not visible"
        )

        back_button.click()

        time.sleep(2)

        print("[PASS] Back button clicked successfully")


