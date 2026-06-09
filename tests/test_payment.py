import pytest
import allure
import json
import time
from pages.payment import PaymentPage
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy

# Load test data
with open("data/payment_data.json") as f:
    test_data = json.load(f)


@allure.feature("Payments")
@allure.story("Create Payment")
class TestPayment:
    @pytest.mark.order(13)
    @pytest.mark.reg
    @allure.title("Create payment and validate in database")
    @allure.description("Validate payment creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("payment", test_data["payments"])
    def test_create_payment_and_db_validation(self, driver, db, payment):

        print("\n========== PAYMENT CREATION TEST STARTED ==========\n")
        print(f"[TEST DATA] {payment}")
        payment_page = PaymentPage(driver)
        sidebar_page = SidebarPage(driver)

        # Step 0 - Close popup if displayed
        with allure.step(" back initial popup"):
            sidebar_page.click_back_button()

        # Step 1 - Open Sidebar
        with allure.step("Side bar menu"):

            sidebar_page.open_sidebar()

        payment_page.navigate_to_payments()
        payment_page.click_enter_payment()

        payment_page.select_client(payment["client_name"])
        payment_page.select_invoice_by_coordinates()
        payment_page.select_payment_method(payment["payment_method"])

        payment_page.enter_transaction_reference(payment["transaction_ref"])
        payment_page.enter_private_notes(payment["private_notes"])
        payment_page.save_payment()

        payment_page.verify_and_print_amounts(
            payment["expected_amount"], payment["expected_applied"]
        )

        # Step 11 - Database Validation
        with allure.step("Validate payment in database"):

            query = """
                    SELECT *
                    FROM payments
                    WHERE transaction_reference = %s
                    ORDER BY id DESC
                        LIMIT 1
                    """

            transaction_ref = payment["transaction_ref"]

            # Using your custom db.fetch_one method
            record = db.fetch_one(query, (transaction_ref,))

            assert record is not None, (
                f"Payment record not found for "
                f"Transaction Reference: {transaction_ref}"
            )

            print("\n========== PAYMENT DATABASE RECORD ==========\n")

            for key, value in record.items():
                print(f"{key}: {value}")

            print("\n=============================================\n")

            # --------------------------------------------------
            # Assertions
            # --------------------------------------------------

            assert (
                record["transaction_reference"].strip()
                == payment["transaction_ref"].strip()
            ), (
                f"Transaction Reference mismatch. "
                f"Expected={payment['transaction_ref']} "
                f"Actual={record['transaction_reference']}"
            )

            assert (
                record["private_notes"].strip() == payment["private_notes"].strip()
            ), (
                f"Private Notes mismatch. "
                f"Expected={payment['private_notes']} "
                f"Actual={record['private_notes']}"
            )

            # Extract decimals from strings like "Amount\n$18,510.75"
            expected_amt = float(
                payment["expected_amount"].split("$")[-1].replace(",", "")
            )

            assert float(record["amount"]) == expected_amt, (
                f"Amount mismatch. "
                f"Expected={expected_amt} "
                f"Actual={record['amount']}"
            )

            expected_applied = float(
                payment["expected_applied"].split("$")[-1].replace(",", "")
            )

            assert float(record["applied"]) == expected_applied, (
                f"Applied mismatch. "
                f"Expected={expected_applied} "
                f"Actual={record['applied']}"
            )

            print(f"Payment ID     : {record['id']}")
            print(f"Client ID      : {record['client_id']}")
            print(f"Amount         : {record['amount']}")
            print(f"Applied        : {record['applied']}")
