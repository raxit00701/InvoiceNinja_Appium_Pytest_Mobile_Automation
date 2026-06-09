import pytest
import allure
import json
import time
import random

from pages.vendors import VendorsPage
from pages.sidebar import SidebarPage

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------------------------------------------------
# Generate Fresh Vendor Test Data
# ---------------------------------------------------------

unique_id = random.randint(100000, 999999)

vendor_data = {
    "vendor": [
        {
            "name": f"Global Freight Logistics {unique_id}",
            "id_number": f"ID-{unique_id}",
            "vat_number": f"VAT-{unique_id}",
            "website": f"https://globalfreight{unique_id}.com",
            "phone": f"98765{unique_id}",
            "contact_first_name": "Sam",
            "contact_last_name": "Tester",
            "contact_email": f"sam{unique_id}@globalfreight.com",
            "contact_phone": f"90000{unique_id}",
            "public_notes": "Preferred logistics vendor for international shipments",
            "private_notes": "Handles fragile cargo with special packaging requirements",
            "address1": "11th Street",
            "address2": "Suite Homes",
            "city": "New York",
            "state": "NY",
            "postal_code": "100001",
            "country": "United States",
        }
    ]
}

# ---------------------------------------------------------
# Save Fresh JSON Data
# ---------------------------------------------------------

with open("data/vendor_data.json", "w") as json_file:

    json.dump(vendor_data, json_file, indent=2)

print("\n========== NEW VENDOR TEST DATA GENERATED ==========\n")

# ---------------------------------------------------------
# Load Test Data
# ---------------------------------------------------------

with open("data/vendor_data.json") as f:

    test_data = json.load(f)

# ---------------------------------------------------------
# Test Class
# ---------------------------------------------------------


@pytest.mark.order(5)
@allure.feature("Vendor")
@allure.story("Create Vendor")
class TestClient:

    @allure.title("Create Vendor and validate in database")
    @allure.description("Validate Vendor creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("vendor", test_data["vendor"])
    def test_create_vendor_and_db_validation(self, driver, db, vendor):

        print(f"\n[TEST DATA] {vendor}")

        wait = WebDriverWait(driver, 20)

        # ---------------------------------------------------------
        # Create Page Objects
        # ---------------------------------------------------------

        sidebar_page = SidebarPage(driver)

        vendors_page = VendorsPage(driver)

        # ---------------------------------------------------------
        # Step 0 - Handle Initial Popup
        # ---------------------------------------------------------
        with allure.step(" clicking Back button"):

            sidebar_page.click_back_button()

        with allure.step("Side bar menu"):
            print("\n[STEP] Side bar menu")
            sidebar_page.open_sidebar()

        # ---------------------------------------------------------
        # Step 1 - Click Vendors
        # ---------------------------------------------------------

        with allure.step("Click Vendors"):
            print("\n[STEP] Click Vendors")
            vendors_page.click_vendors()

        # ---------------------------------------------------------
        # Step 2 - Click New Vendor
        # ---------------------------------------------------------

        with allure.step("Click New Vendor"):
            print("\n[STEP] Click New Vendor")
            vendors_page.click_new_vendor()

        # ---------------------------------------------------------
        # Step 3 - Enter Vendor Name
        # ---------------------------------------------------------

        with allure.step("Enter Vendor Name"):
            print("\n[STEP] Enter Vendor Name")
            vendors_page.enter_vendor_name(vendor["name"])

        # ---------------------------------------------------------
        # Step 4 - Select User
        # ---------------------------------------------------------

        with allure.step("Select User"):
            print("\n[STEP] Select User")
            vendors_page.select_user()

        # ---------------------------------------------------------
        # Step 5 - Enter ID Number
        # ---------------------------------------------------------

        with allure.step("Enter ID Number"):
            print("\n[STEP] Enter ID Number")
            vendors_page.enter_id_number(vendor["id_number"])

        # ---------------------------------------------------------
        # Step 6 - Enter VAT Number
        # ---------------------------------------------------------

        with allure.step("Enter VAT Number"):
            print("\n[STEP] Enter VAT Number")
            vendors_page.enter_vat_number(vendor["vat_number"])

        # ---------------------------------------------------------
        # Step 7 - Enter Website
        # ---------------------------------------------------------

        with allure.step("Enter Website"):
            print("\n[STEP] Enter Website")
            vendors_page.enter_website(vendor["website"])

        # ---------------------------------------------------------
        # Step 8 - Enter Phone
        # ---------------------------------------------------------

        with allure.step("Enter Phone"):
            print("\n[STEP] Enter Phone")
            vendors_page.enter_phone(vendor["phone"])

        # ---------------------------------------------------------
        # Step 9 - Click Tax Exempt
        # ---------------------------------------------------------

        with allure.step("Click Tax Exempt"):
            print("\n[STEP] Click Tax Exempt")
            vendors_page.click_tax_exempt()

        # ---------------------------------------------------------
        # Step 10 - Open Contacts Tab
        # ---------------------------------------------------------

        with allure.step("Open Contacts Tab"):
            print("\n[STEP] Open Contacts Tab")
            vendors_page.open_contacts_tab()

        # ---------------------------------------------------------
        # Step 11 - Enter Contact Details
        # ---------------------------------------------------------

        with allure.step("Enter Contact Details"):
            print("\n[STEP] Enter Contact Details")
            vendors_page.enter_contact_details(
                vendor["contact_first_name"],
                vendor["contact_last_name"],
                vendor["contact_email"],
                vendor["contact_phone"],
            )

        # ---------------------------------------------------------
        # Step 12 - Open Notes Tab
        # ---------------------------------------------------------

        with allure.step("Open Notes Tab"):
            print("\n[STEP] Open Notes Tab")
            vendors_page.open_notes_tab()

        # ---------------------------------------------------------
        # Step 13 - Enter Notes
        # ---------------------------------------------------------

        with allure.step("Enter Notes"):
            print("\n[STEP] Enter Notes")
            vendors_page.enter_notes(vendor["public_notes"], vendor["private_notes"])

        # ---------------------------------------------------------
        # Step 14 - Open Address Tab
        # ---------------------------------------------------------

        with allure.step("Open Address Tab"):
            print("\n[STEP] Open Address Tab")
            vendors_page.open_address_tab()

        # ---------------------------------------------------------
        # Step 15 - Enter Address
        # ---------------------------------------------------------

        with allure.step("Enter Address Details"):
            print("\n[STEP] Enter Address Details")
            vendors_page.enter_address(
                vendor["address1"],
                vendor["address2"],
                vendor["city"],
                vendor["state"],
                vendor["postal_code"],
            )

        # ---------------------------------------------------------
        # Step 16 - Select Country
        # ---------------------------------------------------------

        with allure.step("Select Country"):
            print("\n[STEP] Select Country")
            vendors_page.select_country(vendor["country"])

        # ---------------------------------------------------------
        # Step 17 - Save Vendor
        # ---------------------------------------------------------

        with allure.step("Save Vendor"):
            print("\n[STEP] Save Vendor")
            vendors_page.save_vendor()
            time.sleep(3)

        # ---------------------------------------------------------
        # Step 18 - Upload Document
        # ---------------------------------------------------------

        """with allure.step("Upload Document"):
            print("\n[STEP] Upload Document")
            vendors_page.upload_document()"""

        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        # Step 19 - Database Validation
        # ---------------------------------------------------------

        with allure.step("Validate Vendor in Database"):

            print("\n========== DATABASE VALIDATION " "STARTED ==========\n")

            query = """
                    SELECT
                        id,
                        name,
                        id_number,
                        vat_number,
                        website,
                        phone,
                        address1,
                        address2,
                        city,
                        state,
                        postal_code,
                        private_notes,
                        public_notes,
                        is_tax_exempt
                    FROM vendors
                    WHERE TRIM(name) = TRIM(%s)
                    ORDER BY created_at DESC
                        LIMIT 1
                    """

            params = (vendor["name"],)

            print(f"[DB] Executing Query:\n{query}")
            print(f"[DB] Query Parameters: {params}")

            # ---------------------------------------------------------
            # Retry DB Fetch
            # ---------------------------------------------------------

            result = None

            for attempt in range(15):

                print(f"\n[DB CHECK ATTEMPT {attempt + 1}]")

                try:

                    result = db.fetch_one(query, params)

                    print(f"[DB] Raw Query Result: {result}")

                    if result is not None:

                        print("[DB] Vendor found in database")

                        break

                except Exception as e:

                    print(f"[DB ERROR] {e}")

                print("[DB] Vendor not found yet. " "Waiting 3 seconds...")

                time.sleep(3)

            # ---------------------------------------------------------
            # Validate Record Exists
            # ---------------------------------------------------------

            assert result is not None, (
                f"Vendor '{vendor['name']}' " f"not found in database"
            )

            # ---------------------------------------------------------
            # Core Fields Validation
            # ---------------------------------------------------------

            assert result["name"] == vendor["name"], (
                f"Name mismatch: expected "
                f"'{vendor['name']}', "
                f"got '{result['name']}'"
            )

            assert result["id_number"] == vendor["id_number"], (
                f"ID Number mismatch: expected "
                f"'{vendor['id_number']}', "
                f"got '{result['id_number']}'"
            )

            assert result["vat_number"] == vendor["vat_number"], (
                f"VAT Number mismatch: expected "
                f"'{vendor['vat_number']}', "
                f"got '{result['vat_number']}'"
            )

            assert result["website"] == vendor["website"], (
                f"Website mismatch: expected "
                f"'{vendor['website']}', "
                f"got '{result['website']}'"
            )

            assert result["phone"] == vendor["phone"], (
                f"Phone mismatch: expected "
                f"'{vendor['phone']}', "
                f"got '{result['phone']}'"
            )

            # ---------------------------------------------------------
            # Address Validation
            # ---------------------------------------------------------

            assert result["address1"] == vendor["address1"], "Address1 mismatch"

            assert result["address2"] == vendor["address2"], "Address2 mismatch"

            assert result["city"] == vendor["city"], "City mismatch"

            assert result["state"] == vendor["state"], "State mismatch"

            assert (
                result["postal_code"] == vendor["postal_code"]
            ), "Postal code mismatch"

            # ---------------------------------------------------------
            # Notes Validation
            # ---------------------------------------------------------

            assert (
                result["private_notes"] == vendor["private_notes"]
            ), "Private notes mismatch"

            assert (
                result["public_notes"] == vendor["public_notes"]
            ), "Public notes mismatch"

            # ---------------------------------------------------------
            # Tax Exempt Validation
            # ---------------------------------------------------------

            assert int(result["is_tax_exempt"]) == 1, "Tax exempt mismatch"

            # ---------------------------------------------------------
            # Print DB Values
            # ---------------------------------------------------------

            print("\n========== DATABASE VALUES ==========\n")

            print(f"Vendor ID        : {result['id']}")
            print(f"Vendor Name      : {result['name']}")
            print(f"ID Number        : " f"{result['id_number']}")
            print(f"VAT Number       : " f"{result['vat_number']}")
            print(f"Website          : " f"{result['website']}")
            print(f"Phone            : {result['phone']}")
            print(f"Address1         : " f"{result['address1']}")
            print(f"Address2         : " f"{result['address2']}")
            print(f"City             : {result['city']}")
            print(f"State            : {result['state']}")
            print(f"Postal Code      : " f"{result['postal_code']}")
            print(f"Private Notes    : " f"{result['private_notes']}")
            print(f"Public Notes     : " f"{result['public_notes']}")
            print(f"Tax Exempt       : " f"{result['is_tax_exempt']}")

            print("\n========== DATABASE VALIDATION " "COMPLETED ==========\n")
