import pytest
import allure
import json
import time
from pages.transaction import TransactionPage
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy

# Load test data
with open("data/transaction_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(14)
@allure.feature("Transactions")
@allure.story("Create Transaction")
class TestTransaction:

    @allure.title("Create transaction and validate in database")
    @allure.description("Validate transaction creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("transaction", test_data["transactions"])
    def test_create_transaction_and_db_validation(self, driver, db, transaction):

        print("\n========== TRANSACTION CREATION TEST STARTED ==========\n")
        print(f"[TEST DATA] {transaction}")

        # FIX 1: Consistent variable naming
        transaction_page = TransactionPage(driver)
        sidebar_page = SidebarPage(driver)

        # FIX 2: Extract data from the parameterized 'transaction' dictionary
        test_client = transaction["client_name"]
        test_type = transaction["transaction_type"]
        test_amount = transaction["amount"]
        test_description = transaction["description"]

        # Step 0 - Close popup if displayed
        with allure.step(" back initial popup"):
            sidebar_page.click_back_button()

        # Step 1 - Open Sidebar
        with allure.step("Side bar menu"):

            sidebar_page.open_sidebar()
        # FIX 3: Group the page object actions in their own Allure step
        with allure.step("Create Client and Transaction via UI"):
            transaction_page.open_transactions_menu()
            transaction_page.create_client(client_name=test_client)
            transaction_page.create_transaction(
                client_name=test_client,
                transaction_type=test_type,
                amount=test_amount,
                description=test_description,
            )

        # Step 3 - Database Validation
        with allure.step("Validate transaction in database"):
            query = """
                    SELECT *
                    FROM bank_transactions
                    ORDER BY id DESC
                        LIMIT 1 \
                    """
            record = db.fetch_one(query)

            # Removed the duplicate assertion here
            assert record is not None, f"No transaction found for {test_client}"

            print("\n========== DATABASE RECORD ==========")
            for key, value in record.items():
                print(f"{key}: {value}")
            print("=====================================\n")

            print("\n========== DATABASE VALIDATION ==========")
            print(f"DB ID              : {record['id']}")
            print(f"DB Participant     : {record.get('participant_name', 'N/A')}")
            print(f"DB Amount          : {record['amount']}")
            print(f"DB Description     : {record['description']}")
            print(f"DB Created At      : {record.get('created_at', 'N/A')}")

            print("\n========== EXPECTED VALUES ==========")
            print(f"Client Name        : {test_client}")
            print(f"Amount             : {test_amount}")
            print(f"Description        : {test_description}")
            print(f"Transaction Type   : {test_type}")

            assert float(record["amount"]) == float(
                test_amount
            ), f"Amount mismatch. Expected={test_amount} Actual={record['amount']}"

            assert (
                test_description.strip().lower()
                in str(record["description"]).strip().lower()
            ), f"Description mismatch. Expected={test_description} Actual={record['description']}"

            print("\n[SUCCESS] Database validation passed")
