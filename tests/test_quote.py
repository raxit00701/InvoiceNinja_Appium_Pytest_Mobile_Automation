import pytest
import allure
import json
import time
import random
from pages.quotes import QuotesPage
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder

# Load test data
with open("data/quote_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(7)
@allure.feature("Quotes")
@allure.story("Create Quote")
class TestQuote:

    @allure.title("Create quote and validate in database")
    @allure.description("Validate quote creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("quote", test_data["quotes"])
    def test_create_quote_and_db_validation(self, driver, db, quote):

        print("\n========== QUOTE CREATION TEST STARTED ==========\n")

        quotes_page = QuotesPage(driver)
        sidebar_page = SidebarPage(driver)

        print(f"[TEST DATA] {quote}")

        # Generate unique PO Number
        unique_po = f"PO:{random.randint(100000, 999999)}"

        # Step 0 - Close popup if displayed

        sidebar_page.click_back_button()

        # Step 1 - Open Sidebar
        print("\n[STEP] Side bar menu")
        sidebar_page.open_sidebar()

        # Step 2 - Open Quotes
        sidebar_page.open_quotes_section()

        # Step 3
        quotes_page.click_new_quote()

        # Step 4
        quotes_page.open_company_dropdown()

        # Step 5
        quotes_page.select_company(quote["company"])

        # Step 6
        quotes_page.open_user_dropdown()

        # Step 7
        quotes_page.select_user(quote["user"])

        # Step 8
        quotes_page.enter_quote_date(quote["quote_date"])

        # Step 9
        quotes_page.enter_po_number(unique_po)

        # Step 11
        quotes_page.enter_quantity(quote["quantity"])

        # Step 10
        quotes_page.scroll_down_quickly()

        # Step 12
        quotes_page.select_department(quote["department"])

        # Step 13
        quotes_page.select_category(quote["category"])

        # Step 14
        quotes_page.open_logistics_dropdown()

        # Step 15
        quotes_page.select_test_option()

        # Step 16
        quotes_page.open_logistics_list()

        # Step 17
        quotes_page.select_logistics_company(quote["logistics_company"])

        # Step 18
        quotes_page.edit_item_quantity(quote["item_quantity"])

        # Step 19
        quotes_page.open_contacts_tab()

        # Step 20
        quotes_page.open_items_tab()

        # Step 21
        quotes_page.click_add_item()

        # Step 22
        quotes_page.select_product()

        # Step 23
        quotes_page.click_done()

        # Step 24
        quotes_page.open_notes_tab()

        # Step 25
        quotes_page.enter_note1(quote["note1"])

        # Step 26
        quotes_page.enter_note2(quote["note2"])

        # Step 27
        quotes_page.enter_note3(quote["note3"])

        # Step 28
        quotes_page.enter_note4(quote["note4"])

        # Step 29
        quotes_page.open_pdf_tab()

        # Step 30
        quotes_page.verify_pdf_preview()

        # Step 31
        quotes_page.click_save()
        time.sleep(3)

        # Step 32
        quotes_page.verify_quote_saved_successfully()

        print("\n========== QUOTE CREATION TEST COMPLETED ==========\n")

        # Step 33 - Validate Quote In Database
        with allure.step("Validate quote in database"):

            print("[DB] Starting database validation")

            query = """
                    SELECT
                        po_number,
                        amount,
                        balance,
                        status_id,
                        public_notes,
                        private_notes,
                        terms,
                        footer,
                        company_id,
                        user_id
                    FROM quotes
                    WHERE po_number = %s
                    ORDER BY id DESC
                        LIMIT 1
                    """

            db_quote = None

            # Retry because DB insert may take few seconds
            for attempt in range(10):

                print(f"\n[DB CHECK ATTEMPT {attempt + 1}]")

                db_quote = db.fetch_one(query, (unique_po,))

                print(f"[DB RESULT] {db_quote}")

                if db_quote is not None:

                    print("[DB] Quote record found successfully")

                    break

                print("[DB] Quote not found yet. Waiting 2 seconds...")

                time.sleep(2)

            print(f"[DB] Final Query Result: {db_quote}")

            # ---------------- RECORD EXISTS VALIDATION ----------------

            assert (
                db_quote is not None
            ), f"Quote not found in DB for PO Number: {unique_po}"

            print("[ASSERTION PASSED] Quote exists in DB")

            # ---------------- STATUS VALIDATION ----------------

            # Example Mapping
            # Draft = 1
            # Sent = 2
            # Approved = 3

            expected_status = 1

            assert db_quote["status_id"] == expected_status, f"""
                Status Mismatch
                Expected: {expected_status}
                Actual: {db_quote['status_id']}
            """

            print("[ASSERTION PASSED] Status matched")

            # ---------------- PO NUMBER VALIDATION ----------------

            assert db_quote["po_number"] == unique_po, f"""
                PO Number Mismatch
                Expected: {unique_po}
                Actual: {db_quote['po_number']}
            """

            print("[ASSERTION PASSED] PO Number matched")
            # ---------------- TERMS VALIDATION ----------------

            assert db_quote["terms"] == quote["note1"], f"""
                Terms Mismatch
                Expected: {quote['note1']}
                Actual: {db_quote['terms']}
            """

            print("[ASSERTION PASSED] Public Notes matched")

            # ---------------- PRIVATE NOTES VALIDATION ----------------

            assert db_quote["private_notes"] == quote["note4"], f"""
                Private Notes Mismatch
                Expected: {quote['note4']}
                Actual: {db_quote['private_notes']}
            """

            print("[ASSERTION PASSED] Private Notes matched")

            # ---------------- FOOTER VALIDATION ----------------

            assert db_quote["footer"] == quote["note2"], f"""
                Footer Mismatch
                Expected: {quote['note2']}
                Actual: {db_quote['footer']}
            """

            print("[ASSERTION PASSED] Footer matched")

            # ---------------- AMOUNT VALIDATION ----------------

            actual_amount = float(db_quote["amount"])

            assert actual_amount > 0, f"""
                Amount Validation Failed
                Expected amount > 0
                Actual: {actual_amount}
            """

            print("[ASSERTION PASSED] Amount validated")

            # ---------------- BALANCE VALIDATION ----------------

            # ---------------- BALANCE VALIDATION ----------------

            actual_amount = float(db_quote["amount"])
            actual_balance = float(db_quote["balance"])

            # For quotes, Invoice Ninja stores balance as 0
            expected_balance = 0.0

            assert actual_balance == expected_balance, f"""
                Balance Mismatch
                Expected Balance: {expected_balance}
                Actual Balance: {actual_balance}
            """

            print("[ASSERTION PASSED] Balance matched")

            print("[DB] Database validation completed successfully")

        print("\n========== QUOTE CREATION TEST COMPLETED ==========\n")
