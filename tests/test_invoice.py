import pytest
import allure
import json
import time
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy
from pages.invoice import InvoicePage  # Import your new Page Object

# Load test data
with open("data/invoice_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(12)
@pytest.mark.reg
@allure.feature("Invoices")
@allure.story("Create Invoice")
class TestInvoice:

    @allure.title("Create invoice")
    @allure.description("Validate invoice creation flow")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("invoice", test_data["invoices"])
    def test_create_invoice(self, driver, db, invoice):

        print("\n========== INVOICE CREATION TEST STARTED ==========\n")
        print(f"[TEST DATA] {invoice}")
        invoice_page = InvoicePage(driver)
        sidebar_page = SidebarPage(driver)
        # Step 0 - Close the popup
        with allure.step("Close  popup"):
            sidebar_page.click_back_button()

        # Step 1 - Open Sidebar
        with allure.step("Open menu sidebar"):
            sidebar_page.open_sidebar()

        # =========================================================
        # PAGE OBJECT IMPLEMENTATION (Steps 2 - 25)
        # =========================================================
        print("\n[UI] Executing Page Object Model steps...")

        # Instantiate the page object

        # Execute the flow
        invoice_page.open_invoices_section()
        invoice_page.create_new_invoice()
        invoice_page.add_invoice_item()
        invoice_page.fill_invoice_details(invoice)
        invoice_page.open_contacts_tab()
        invoice_page.fill_invoice_notes(invoice)
        invoice_page.verify_pdf_and_save()
        invoice_page.verify_invoice_totals()

        # =========================================================
        # Step 26 - Validate Database
        # =========================================================
        with allure.step("Validate invoice in database"):

            print("\n[DB] Querying database for the latest invoice...")

            # Query to fetch the most recent invoice created
            query = """
                    SELECT *
                    FROM invoices
                    ORDER BY id DESC
                        LIMIT 1 \
                    """

            # Using fetch_one() as it returns a single dictionary which is easier to assert
            record = db.fetch_one(query)

            assert record is not None, "No records found in invoices table"

            # Print raw database dictionary
            print("\n========== RAW DATABASE RECORD ==========")
            for key, value in record.items():
                print(f"{key}: {value}")
            print("=========================================\n")

            # Print mapped comparisons
            print("\n========== DATABASE VALIDATION ==========")
            print(f"DB ID              : {record['id']}")
            print(f"DB PO Number       : {record['po_number']}")
            print(f"DB Discount        : {record['discount']}")
            print(f"DB Invoice Date    : {record['date']}")
            print(f"DB Due Date        : {record['due_date']}")
            print(f"DB Partial Amount  : {record['partial']}")
            print(f"DB Terms           : {record['terms']}")
            print(f"DB Footer          : {record['footer']}")
            print(f"DB Public Notes    : {record['public_notes']}")
            print(f"DB Private Notes   : {record['private_notes']}")

            print("\n========== EXPECTED VALUES (JSON) ==========")
            print(f"PO Number          : {invoice['po_number']}")
            print(f"Discount           : {invoice['discount']}")
            print(f"Invoice Date       : {invoice['invoice_date']}")
            print(f"Due Date           : {invoice['due_date']}")
            print(f"Partial Amount     : {invoice['partial_amount']}")
            print(f"Terms              : {invoice['invoice_terms']}")
            print(f"Footer             : {invoice['invoice_footer']}")
            print(f"Public Notes       : {invoice['public_notes']}")
            print(f"Private Notes      : {invoice['private_notes']}")

            # =========================================================
            # Assertions
            # =========================================================

            # Basic String Comparisons
            assert str(record["po_number"]) == str(
                invoice["po_number"]
            ), f"PO Number mismatch. Expected={invoice['po_number']} Actual={record['po_number']}"

            # Date Comparisons
            assert str(record["date"]) == str(
                invoice["invoice_date"]
            ), f"Invoice Date mismatch. Expected={invoice['invoice_date']} Actual={record['date']}"

            # Float/Number Comparisons
            assert float(record["discount"]) == float(
                invoice["discount"]
            ), f"Discount mismatch. Expected={invoice['discount']} Actual={record['discount']}"
            assert float(record["partial"]) == float(
                invoice["partial_amount"]
            ), f"Partial Amount mismatch. Expected={invoice['partial_amount']} Actual={record['partial']}"

            # Text Area Comparisons (Using 'in' and strip() to avoid formatting/newline flakiness)
            assert (
                invoice["invoice_terms"].strip() in str(record["terms"]).strip()
            ), f"Terms mismatch. Expected={invoice['invoice_terms']} Actual={record['terms']}"
            assert (
                invoice["invoice_footer"].strip() in str(record["footer"]).strip()
            ), f"Footer mismatch. Expected={invoice['invoice_footer']} Actual={record['footer']}"
            '''assert (
                invoice["public_notes"].strip() in str(record["public_notes"]).strip()
            ), f"Public notes mismatch. Expected={invoice['public_notes']} Actual={record['public_notes']}"'''
            assert (
                invoice["private_notes"].strip() in str(record["private_notes"]).strip()
            ), f"Private notes mismatch. Expected={invoice['private_notes']} Actual={record['private_notes']}"

            print("\n[SUCCESS] Invoice database validation completely passed!")
