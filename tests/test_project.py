import pytest
import allure
import json
import time
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy
from pages.projects import ProjectsPage

# Load test data
with open("data/project_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(4)
@allure.feature("Project")
@allure.story("Create Project")
class TestClient:
    @allure.title("Create Project and validate in database")
    @allure.description("Validate Project creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("project", test_data["project"])
    def test_create_project_and_db_validation(self, driver, db, project):

        print("\n========== PROJECT CREATION TEST STARTED ==========\n")

        sidebar_page = SidebarPage(driver)
        projects_page = ProjectsPage(driver)

        # ---------------------------------------------------------
        # Step 0 - Close popup if displayed
        # ---------------------------------------------------------
        with allure.step(" clicking Back button"):

            sidebar_page.click_back_button()
        # ---------------------------------------------------------
        # Step 1.1 - Click on Sidebar
        with allure.step("Side bar menu"):
            sidebar_page.open_sidebar()
        # ---------------------------------------------------------

        # Step 2 - Open Projects
        with allure.step("Open Projects section"):
            sidebar_page.open_projects_section()

        # Step 3 - Click New Project
        with allure.step("Click New Project"):
            projects_page.click_new_project()

        # Step 4 - Enter Project Name
        with allure.step("Enter Project Name"):
            projects_page.enter_project_name(project["project_name"])

        # Step 5 - Select Company
        with allure.step("Select Company"):
            projects_page.select_company(project["company_name"])

        # Step 6 - Select User
        with allure.step("Select User"):
            projects_page.select_user(project["user_name"])

        # Step 7 - Enter Date
        with allure.step("Enter Date"):
            projects_page.enter_date(project["date"])

        # Step 8 - Enter Amount
        with allure.step("Enter Amount"):
            projects_page.enter_amount(project["amount"])

        # Step 9 - Enter Tax
        with allure.step("Enter Tax"):
            projects_page.enter_tax(project["tax"])

        # Step 10 - Enter Description
        with allure.step("Enter Description"):
            projects_page.enter_description(project["description"])

        # Step 11 - Enter Notes
        with allure.step("Enter Notes"):
            projects_page.enter_notes(project["notes"])

        # Step 12 - Save Project
        with allure.step("Save Project"):
            projects_page.click_save()
            time.sleep(3)

        # Step 13 - Verify Invoice Project
        with allure.step("Verify Invoice Project"):
            projects_page.verify_invoice_project()

        print("\n========== PROJECT CREATED SUCCESSFULLY ==========\n")

        # Step 13 - Validate Project in Database
        with allure.step("Validate Project data in database"):
            print("[DB] Validating project in database")

            query = """
                    SELECT
                        name,
                        task_rate,
                        private_notes,
                        public_notes
                    FROM projects
                    WHERE name = %s
                    ORDER BY id DESC
                        LIMIT 1
                    """

            result = db.fetch_one(query, (project["project_name"],))

            # Print full DB result
            print(f"[DB RESULT] Exact data from DB: {result}")

            # Check if project already exists
            if result:
                print("[DB] Project data already exists in database")
            else:
                print("[DB] Project record not found in database")

            assert result is not None, "Project record not found in database"

            # Database values
            db_project_name = result["name"]
            db_task_rate = str(result["task_rate"])
            db_private_notes = result["private_notes"]
            db_public_notes = result["public_notes"]

            # Print extracted values clearly
            print("----------- DB VALUES -----------")
            print(f"Project Name   : {db_project_name}")
            print(f"Task Rate      : {db_task_rate}")
            print(f"Private Notes  : {db_private_notes}")
            print(f"Public Notes   : {db_public_notes}")
            print("---------------------------------")

            # Assertions
            assert (
                db_project_name == project["project_name"]
            ), f"Expected project name {project['project_name']} but got {db_project_name}"

            assert db_task_rate.startswith(
                str(project["amount"])
            ), f"Expected amount {project['amount']} but got {db_task_rate}"

            assert (
                db_private_notes == project["notes"]
            ), f"Expected notes {project['notes']} but got {db_private_notes}"

            assert (
                db_public_notes == project["description"]
            ), f"Expected description {project['description']} but got {db_public_notes}"

            print("[DB] Project validation successful")
