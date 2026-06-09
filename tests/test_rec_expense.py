import pytest
import allure
import json
import time
from pages.recur_expense import RecurringExpensePage
from pages.sidebar import SidebarPage


from appium.webdriver.common.appiumby import AppiumBy

# Load test data
with open("data/recurring_expense_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(9)
@pytest.mark.reg
@allure.feature("Recurring Expense")
@allure.story("Create Recurring Expense")
class TestRecurringExpense:

    @allure.title("Create recurring expense and validate in database")
    @allure.description(
        "Validate recurring expense creation flow and database validation"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("recurring_expense", test_data["recurring_expenses"])
    def test_create_recurring_expense_and_db_validation(
        self, driver, db, recurring_expense
    ):
        recurring_expense_page = RecurringExpensePage(driver)
        sidebar_page = SidebarPage(driver)

        print("\n========== RECURRING EXPENSE CREATION TEST STARTED ==========\n")
        print(f"[TEST DATA] {recurring_expense}")

        # Step 0 - Close the popup
        sidebar_page.click_back_button()

        # Step 1 - Open Sidebar
        sidebar_page.open_sidebar()

        with allure.step("Open Recurring Expense section"):
            recurring_expense_page.open_recurring_expense_menu()

        with allure.step("Create new recurring expense"):
            recurring_expense_page.click_new_recurring_expense()

        with allure.step("Select customer"):
            recurring_expense_page.select_customer(recurring_expense["customer"])

        with allure.step("Select vendor"):
            recurring_expense_page.select_vendor(recurring_expense["vendor"])

        with allure.step("Select expense account"):
            recurring_expense_page.select_expense_account(
                recurring_expense["expense_account"]
            )

        with allure.step("Select category"):
            recurring_expense_page.select_category(recurring_expense["category"])

        with allure.step("Assign user"):
            recurring_expense_page.select_user(recurring_expense["user"])

        with allure.step("Enter amount"):
            recurring_expense_page.enter_amount(recurring_expense["amount"])

        with allure.step("Add notes"):
            recurring_expense_page.add_notes(
                recurring_expense["public_note"],
                recurring_expense["private_note"],
            )

        with allure.step("Open settings"):
            recurring_expense_page.open_settings_tab()

        with allure.step("Enable document visibility"):
            recurring_expense_page.enable_document_visibility()

        with allure.step("Save recurring expense"):
            recurring_expense_page.save()

        with allure.step("Validate recurring expense created"):
            recurring_expense_page.verify_recurring_expense_created(
                recurring_expense["amount"]
            )

        with allure.step("Validate recurring expense in database"):

            print("\n========== DATABASE VALIDATION ==========\n")

            query = """
                    SELECT
                        amount,
                        public_notes,
                        private_notes
                    FROM recurring_expenses
                    ORDER BY id DESC
                        LIMIT 1 \
                    """

            db_record = db.fetch_one(query)

            assert db_record is not None, "No recurring expense record found in DB"

            print(f"[DB] Amount       : {db_record['amount']}")
            print(f"[DB] Public Note  : {db_record['public_notes']}")
            print(f"[DB] Private Note : {db_record['private_notes']}")

            assert float(db_record["amount"]) == float(recurring_expense["amount"]), (
                f"Amount mismatch. Expected={recurring_expense['amount']} "
                f"Actual={db_record['amount']}"
            )

            assert db_record["public_notes"] == recurring_expense["public_note"], (
                f"Public note mismatch. Expected='{recurring_expense['public_note']}' "
                f"Actual='{db_record['public_notes']}'"
            )

            assert db_record["private_notes"] == recurring_expense["private_note"], (
                f"Private note mismatch. Expected='{recurring_expense['private_note']}' "
                f"Actual='{db_record['private_notes']}'"
            )

            print("\n[PASS] Recurring expense database validation successful")
