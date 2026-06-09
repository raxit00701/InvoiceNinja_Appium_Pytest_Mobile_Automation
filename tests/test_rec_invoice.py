import pytest
import allure
import json
import time
from pages.rec_invoice import RecurringInvoicePage
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy

# Load test data
with open("data/recurring_invoice_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(11)
@allure.feature("Recurring Invoices")
@allure.story("Create Recurring Invoice")
class TestRecurringInvoice:

    @allure.title("Create recurring invoice and validate in database")
    @allure.description(
        "Validate recurring invoice creation flow and database validation"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("invoice", test_data["recurring_invoices"])
    def test_create_recurring_invoice_and_db_validation(self, driver, db, invoice):

        print("\n========== INVOICE CREATION TEST STARTED ==========\n")
        print(f"[TEST DATA] {invoice}")
        recurinvoicepage = RecurringInvoicePage(driver)

        sidebar_page = SidebarPage(driver)

        sidebar_page.click_back_button()

        # Step 0 - Close popup if present
        sidebar_page.open_sidebar()

        recurinvoicepage.click_new_recurring_invoice()

        recurinvoicepage.select_client(invoice["client"])

        recurinvoicepage.select_user()

        recurinvoicepage.scroll_to_frequency()

        recurinvoicepage.enter_po_number(invoice["po_number"])

        recurinvoicepage.enter_discount(invoice["discount"])

        recurinvoicepage.enable_auto_bill()

        recurinvoicepage.select_design(invoice["design"])

        recurinvoicepage.select_vendor(invoice["vendor"])

        recurinvoicepage.select_expense_account("test")

        recurinvoicepage.open_contacts_tab()

        recurinvoicepage.open_items_tab()

        recurinvoicepage.add_item()

        recurinvoicepage.open_notes_tab()

        recurinvoicepage.enter_notes(
            invoice["invoice_terms"],
            invoice["invoice_footer"],
            invoice["public_notes"],
            invoice["private_notes"],
        )

        recurinvoicepage.open_pdf_tab()

        recurinvoicepage.verify_pdf_preview()

        recurinvoicepage.save()

        recurinvoicepage.verify_invoice_created(invoice["expected_amount"])

        with allure.step("Validate recurring invoice in database"):

            query = """
                    SELECT *
                    FROM recurring_invoices
                    WHERE po_number = %s
                    ORDER BY id DESC
                        LIMIT 1 \
                    """

            record = db.fetch_one(query, (invoice["po_number"],))

            assert record is not None, (
                f"Recurring Invoice not found for " f"PO Number: {invoice['po_number']}"
            )

            print("\n========== RECURRING INVOICE DATABASE RECORD ==========\n")

            for key, value in record.items():
                print(f"{key}: {value}")

            print("\n=====================================================\n")

            # --------------------------------------------------
            # Assertions
            # --------------------------------------------------

            assert record["po_number"] == invoice["po_number"], (
                f"PO Number mismatch. "
                f"Expected={invoice['po_number']} "
                f"Actual={record['po_number']}"
            )

            assert float(record["discount"]) == float(invoice["discount"]), (
                f"Discount mismatch. "
                f"Expected={invoice['discount']} "
                f"Actual={record['discount']}"
            )

            assert record["terms"].strip() == invoice["invoice_terms"].strip(), (
                f"Invoice Terms mismatch. "
                f"Expected={invoice['invoice_terms']} "
                f"Actual={record['terms']}"
            )

            assert record["footer"].strip() == invoice["invoice_footer"].strip(), (
                f"Invoice Footer mismatch. "
                f"Expected={invoice['invoice_footer']} "
                f"Actual={record['footer']}"
            )

            """assert record["public_notes"].strip() == invoice["public_notes"].strip(), (
                f"Public Notes mismatch. "
                f"Expected={invoice['public_notes']} "
                f"Actual={record['public_notes']}"
            )"""

            assert (
                record["private_notes"].strip() == invoice["private_notes"].strip()
            ), (
                f"Private Notes mismatch. "
                f"Expected={invoice['private_notes']} "
                f"Actual={record['private_notes']}"
            )
            print(f"Client ID      : {record['client_id']}")
            print(f"Vendor ID      : {record['vendor_id']}")
            print(f"Design ID      : {record['design_id']}")
            print(f"Amount         : {record['amount']}")
            print(f"Balance        : {record['balance']}")
            print(f"Frequency ID   : {record['frequency_id']}")
            print(f"Auto Bill      : {record['auto_bill']}")
            print(f"Created At     : {record['created_at']}")

            print("\n[SUCCESS] Recurring Invoice Database Validation Passed")

            print("\n=====================================================\n")
