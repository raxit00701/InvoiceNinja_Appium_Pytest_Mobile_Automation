import pytest
import allure
import json
import time
from pages.purchase_orders import PurchaseOrdersPage
from appium.webdriver.common.appiumby import AppiumBy
from pages.sidebar import SidebarPage

# Load test data
with open("data/purchase_order_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(10)
@allure.feature("Purchase Orders")
@allure.story("Create Purchase Order")
class TestPurchaseOrder:

    @allure.title("Create purchase order and validate in database")
    @allure.description("Validate purchase order creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("purchase_order", test_data["purchase_orders"])
    def test_create_purchase_order_and_db_validation(self, driver, db, purchase_order):

        print("\n========== PURCHASE ORDER CREATION TEST STARTED ==========\n")
        print(f"[TEST DATA] {purchase_order}")
        purchase_orders_page = PurchaseOrdersPage(driver)
        sidebar_page = SidebarPage(driver)

        # Step 0 - Close the popup
        sidebar_page.click_back_button()

        # Step 1 - Open Sidebar
        sidebar_page.open_sidebar()

        purchase_orders_page.open_purchase_orders_menu()
        purchase_orders_page.click_new_purchase_order()
        purchase_orders_page.select_vendor(purchase_order["vendor"])
        purchase_orders_page.select_user(purchase_order["user"])
        purchase_orders_page.enter_due_date(purchase_order["due_date"])
        purchase_orders_page.enter_discount(purchase_order["discount"])
        purchase_orders_page.enter_shipping_cost(purchase_order["shipping_cost"])
        purchase_orders_page.scroll_to_item_section()
        purchase_orders_page.select_design(purchase_order["design"])
        purchase_orders_page.select_client(purchase_order["client"])
        purchase_orders_page.select_expense_account(purchase_order["expense_account"])
        purchase_orders_page.open_contacts_tab()
        purchase_orders_page.open_items_tab()
        purchase_orders_page.add_item()
        purchase_orders_page.open_notes_tab()

        purchase_orders_page.enter_notes(
            purchase_order["invoice_terms"],
            purchase_order["invoice_footer"],
            purchase_order["public_notes"],
            purchase_order["private_notes"],
        )

        purchase_orders_page.open_pdf_tab()
        purchase_orders_page.save()

        purchase_orders_page.verify_purchase_order_created(
            purchase_order["expected_amount"]
        )
        #   STEP 21: DB VALIDATION

        with allure.step("Validate purchase order in database"):

            print("\n========== DATABASE VALIDATION ==========\n")

            query = """
                    SELECT *
                    FROM purchase_orders
                    ORDER BY id DESC
                        LIMIT 1 \
                    """

            db_record = db.fetch_one(query)

            assert db_record is not None, "No Purchase Order record found in database"

            print("\n========== PURCHASE ORDER DATABASE RECORD ==========\n")

            for column, value in db_record.items():
                print(f"[DB] {column:<30}: {value}")

            print("\n========== VALIDATING REQUIRED FIELDS ==========\n")

            expected_amount = float(
                purchase_order["expected_amount"].replace("$", "").replace(",", "")
            )

            assert float(db_record["amount"]) == expected_amount, (
                f"Amount mismatch. "
                f"Expected={expected_amount}, "
                f"Actual={db_record['amount']}"
            )

            assert db_record["terms"] == purchase_order["invoice_terms"], (
                f"Terms mismatch. "
                f"Expected='{purchase_order['invoice_terms']}', "
                f"Actual='{db_record['terms']}'"
            )

            assert db_record["footer"] == purchase_order["invoice_footer"], (
                f"Footer mismatch. "
                f"Expected='{purchase_order['invoice_footer']}', "
                f"Actual='{db_record['footer']}'"
            )

            assert db_record["public_notes"] == purchase_order["public_notes"], (
                f"Public Notes mismatch. "
                f"Expected='{purchase_order['public_notes']}', "
                f"Actual='{db_record['public_notes']}'"
            )

            assert db_record["private_notes"] == purchase_order["private_notes"], (
                f"Private Notes mismatch. "
                f"Expected='{purchase_order['private_notes']}', "
                f"Actual='{db_record['private_notes']}'"
            )

            print("\n[PASS] Purchase Order database validation successful")
