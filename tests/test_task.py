import pytest
import allure
import json
import time
from pages.tasks import TasksPage
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

# Load test data
with open("data/task_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(6)
@allure.feature("Tasks")
@allure.story("Create Tasks")
class TestTask:

    @allure.title("Create task and validate in database")
    @allure.description("Validate task creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("task", test_data["tasks"])
    def test_create_task_and_db_validation(self, driver, db, task):
        tasks_page = TasksPage(driver)
        sidebar_page = SidebarPage(driver)

        print("\n========== TASK CREATION TEST STARTED ==========\n")

        wait = WebDriverWait(driver, 20)

        print(f"[TEST DATA] {task}")

        # Step 0 - Close popup if displayed
        with allure.step(" back initial popup"):
            sidebar_page.click_back_button()

        # Step 1 - Open Sidebar
        with allure.step("Side bar menu"):

            sidebar_page.open_sidebar()

        # Step 2 - Open Tasks
        with allure.step("Open Task Section"):
            sidebar_page.open_tasks_section()
        # Step 3
        with allure.step("Click New Task"):

            tasks_page.click_new_task()

        # Step 4 + 5
        with allure.step("Select Client"):

            tasks_page.select_client(task["client_name"])

        # Step 6 + 7
        with allure.step("Select Project"):

            tasks_page.select_project(task["project_name"])

        # Step 8
        with allure.step("Select User"):

            tasks_page.select_user(task["user_name"])

        # Step 9
        with allure.step("Enter Task Number"):

            unique_task_number = tasks_page.enter_task_number()

        # Step 10
        with allure.step("Enter Cost"):

            tasks_page.enter_cost(task["cost"])

        # Step 11
        with allure.step("Change Task Status"):

            tasks_page.change_status(task["status"])

        # Step 12
        with allure.step("Enter Description"):

            tasks_page.enter_description(task["description"])

        # Step 13
        with allure.step("Open Times Tab"):

            tasks_page.open_times_tab()

        # Step 14
        with allure.step("Start Timer"):

            tasks_page.start_timer()

        # Step 15
        with allure.step("Stop Timer"):

            tasks_page.stop_timer()

        # Step 16
        with allure.step("Save Task"):

            tasks_page.save_task()
            time.sleep(3)

        # Step 17
        with allure.step("Open Overview Tab"):

            tasks_page.open_overview_tab()

        # Step 18
        with allure.step("Open Documents Tab"):

            tasks_page.open_documents_tab()

        # Step 19
        with allure.step("Upload File"):

            tasks_page.upload_file()

        # Step 20 - Validate Task In Database
        with allure.step("Validate task in database"):

            print("[DB] Starting database validation")

            query = """
                    SELECT
                        number,
                        rate,
                        description,
                        status_id
                    FROM tasks
                    WHERE number = %s
                    ORDER BY id DESC
                        LIMIT 1 \
                    """

            db_task = None

            for attempt in range(10):

                print(f"\n[DB CHECK ATTEMPT {attempt + 1}]")

                db_task = db.fetch_one(query, (unique_task_number,))

                print(f"[DB RESULT] {db_task}")

                if db_task is not None:

                    print("[DB] Record found successfully")

                    break

                print("[DB] Record not found yet. Waiting 2 seconds...")

                time.sleep(2)

            print(f"[DB] Query Result: {db_task}")

            # Validate task exists
            assert (
                db_task is not None
            ), f"Task not found in DB for number: {unique_task_number}"

            print("[ASSERTION PASSED] Task exists in DB")

            # Status Mapping
            status_mapping = {"Backlog": 1, "In progress": 3, "Done": 4}

            expected_status = status_mapping.get(task["status"])

            # Validate task number
            assert db_task["number"] == unique_task_number, f"""
                Task Number Mismatch
                Expected: {unique_task_number}
                Actual: {db_task['number']}
            """

            print("[ASSERTION PASSED] Task number matched")

            # Validate rate
            expected_rate = float(task["cost"].replace("$", ""))

            actual_rate = float(db_task["rate"])

            assert actual_rate == expected_rate, f"""
                Rate Mismatch
                Expected: {expected_rate}
                Actual: {actual_rate}
            """

            print("[ASSERTION PASSED] Rate matched")

            # Validate description
            assert db_task["description"] == task["description"], f"""
                Description Mismatch
                Expected: {task['description']}
                Actual: {db_task['description']}
            """

            print("[ASSERTION PASSED] Description matched")

            # Validate status
            assert db_task["status_id"] == expected_status, f"""
                Status Mismatch
                Expected: {expected_status}
                Actual: {db_task['status_id']}
            """

            print("[ASSERTION PASSED] Status matched")

            print("[DB] Database validation completed successfully")

        print("\n========== TASK CREATION TEST COMPLETED ==========\n")
