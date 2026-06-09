import time

from appium.webdriver.common.appiumby import AppiumBy


class TasksPage:

    def __init__(self, driver):

        self.driver = driver

    # Step 3
    def click_new_task(self):

        print("[UI] Looking for New Task button")

        el1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "New Task")

        print("[UI] Clicking New Task")

        el1.click()

        time.sleep(0.5)

    # Step 4 + 5
    def select_client(self, client_name):

        print("[UI] Opening Client dropdown")

        el2 = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.View").instance(18)',
        )

        el2.click()

        time.sleep(0.5)

        print(f"[UI] Selecting client: {client_name}")

        client = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, client_name)

        client.click()

        time.sleep(0.5)

    # Step 6 + 7
    def select_project(self, project_name):

        print("[UI] Opening Project dropdown")

        el4 = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.View").instance(19)',
        )

        el4.click()

        time.sleep(0.5)

        print(f"[UI] Selecting project: {project_name}")

        project = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{project_name}").instance(0)',
        )

        project.click()

        time.sleep(0.5)

    # Step 8
    def select_user(self, user_name):

        print("[UI] Clicking User dropdown")

        el6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "User")

        el6.click()

        time.sleep(0.5)

        print(f"[UI] Selecting user: {user_name}")

        el7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, user_name)

        el7.click()

        time.sleep(0.5)

    # Step 9
    def enter_task_number(self):

        unique_task_number = f"TN:{int(time.time())}"

        print(f"[UI] Entering task number: {unique_task_number}")

        el8 = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(0)',
        )

        el8.click()

        el8.send_keys(unique_task_number)

        time.sleep(0.5)

        return unique_task_number

    # Step 10
    def enter_cost(self, cost):

        print(f"[UI] Entering cost: {cost}")

        el9 = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)',
        )

        el9.click()

        el9.send_keys(cost)

        time.sleep(0.5)

    # Step 11
    def change_status(self, status_name):

        print("[UI] Waiting before tapping Status dropdown")

        time.sleep(1.5)

        print("[UI] Tapping on Status dropdown coordinates: (360, 923)")

        self.driver.tap([(360, 923)])

        time.sleep(0.5)

        print(f"[UI] Selecting status: {status_name}")

        status = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, status_name)

        status.click()

        time.sleep(0.5)

        print("[UI] Status selected successfully")

    # Step 12
    def enter_description(self, description):

        print(f"[UI] Entering description: {description}")

        el12 = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(2)',
        )

        el12.click()

        el12.send_keys(description)

        time.sleep(0.5)

    # Step 13
    def open_times_tab(self):

        print("[UI] Opening Times tab")

        el13 = self.driver.find_element(
            AppiumBy.XPATH, '//android.view.View[@content-desc="Times\nTab 2 of 2"]'
        )

        el13.click()

        time.sleep(0.5)

    # Step 14
    def start_timer(self):

        print("[UI] Clicking Start button")

        el14 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Start")

        el14.click()

        time.sleep(3)

    # Step 15
    def stop_timer(self):

        print("[UI] Clicking Stop button")

        el15 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Stop")

        el15.click()

        time.sleep(0.5)

    # Step 16
    def save_task(self):

        print("[UI] Clicking Save button")

        el16 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Save")

        el16.click()

        time.sleep(3)

    # Step 17
    def open_overview_tab(self):

        print("[UI] Opening Overview tab")

        el17 = self.driver.find_element(
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="Overview\nTab 1 of 2"]',
        )

        el17.click()

        time.sleep(0.5)

    # Step 18
    def open_documents_tab(self):

        print("[UI] Opening Documents tab")

        el18 = self.driver.find_element(
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="Documents\nTab 2 of 2"]',
        )

        el18.click()

        time.sleep(0.5)

    # Step 19
    def upload_file(self):

        print("[UI] Clicking Upload Files button")

        el19 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Upload Files")

        el19.click()

        time.sleep(3)

        print("[UI] Selecting file from device")

        el20 = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.google.android.documentsui:id/icon_thumb").instance(0)',
        )

        el20.click()

        time.sleep(3)
