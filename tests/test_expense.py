import pytest
import allure
import json
import time
from pages.expenses import ExpensesPage
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

# Load test data
with open("data/expense_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(8)
@pytest.mark.reg
@allure.feature("Expenses")
@allure.story("Create Expense")
class TestExpense:

    @allure.title("Create expense and validate in database")
    @allure.description("Validate expense creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("expense", test_data["expenses"])
    def test_create_expense_and_db_validation(self, driver, db, expense):

        print("\n========== EXPENSE CREATION TEST STARTED ==========\n")
        print(f"[TEST DATA] {expense}")
        expense_page = ExpensesPage(driver)
        sidebar_page = SidebarPage(driver)

        sidebar_page.click_back_button()

        # Step 0 - Close popup if present
        sidebar_page.open_sidebar()

        # Step 1 - Open Sidebar

        expense_page.open_expenses()

        expense_page.click_new_expense()

        expense_page.select_customer(expense["customer"])

        expense_page.select_project(expense["project"])

        expense_page.select_expense_type(expense["expense_type"])

        expense_page.select_category(expense["category"])

        expense_page.select_user()

        expense_page.enter_amount(expense["amount"])

        expense_page.open_notes_tab()

        expense_page.enter_notes(expense["notes"])

        expense_page.enter_vendor_notes(expense["vendor_notes"])

        expense_page.open_settings_tab()

        expense_page.enable_should_be_invoiced()

        expense_page.enable_add_documents_to_invoice()

        expense_page.save()

        expense_page.verify_expense_created(expense["customer"])

        with allure.step("Validate expense in database"):

            print("\n[DB] Starting expense validation")

            query = """
                    SELECT
                        amount,
                        private_notes,
                        public_notes
                    FROM expenses
                    WHERE amount = %s
                      AND private_notes = %s
                      AND public_notes = %s
                    ORDER BY id DESC
                        LIMIT 1 \
                    """

            db_expense = None

            for attempt in range(10):

                print(f"\n[DB CHECK ATTEMPT {attempt + 1}]")

                db_expense = db.fetch_one(
                    query,
                    (
                        expense["amount"],
                        expense["vendor_notes"],
                        expense["notes"],
                    ),
                )

                print(f"[DB RESULT] {db_expense}")

                if db_expense is not None:

                    print("[DB] Expense record found successfully")

                    break

                print("[DB] Expense not found yet. Waiting 2 seconds...")

                time.sleep(2)

            print(f"[DB] Final Query Result: {db_expense}")

            assert db_expense is not None, (
                f"Expense record not found in DB.\n"
                f"Amount: {expense['amount']}\n"
                f"Private Notes: {expense['vendor_notes']}\n"
                f"Public Notes: {expense['notes']}"
            )

            assert float(db_expense["amount"]) == float(expense["amount"])
            assert db_expense["private_notes"] == expense["vendor_notes"]
            assert db_expense["public_notes"] == expense["notes"]

            print("[PASS] Expense validated successfully in database")
