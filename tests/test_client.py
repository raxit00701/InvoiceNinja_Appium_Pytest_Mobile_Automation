import pytest
import allure
import json
import time
import random


from pages.client import ClientPage
from pages.sidebar import SidebarPage
from appium.webdriver.common.appiumby import AppiumBy


def generate_client_data():

    unique_id = random.randint(100000, 999999)

    client_data = {
        "clients": [
            {
                "name": f"Nova Digital Systems {unique_id}",
                "id_number": f"ID-{unique_id}",
                "vat_number": f"VAT-{unique_id}",
                "website": f"https://novadigital{unique_id}.com",
                "phone": f"+1-555-{unique_id}",
                "contacts": {
                    "first_name": "Michael",
                    "last_name": "Brown",
                    "email": f"michael{unique_id}@novadigital.com",
                    "phone": f"+1-555-{unique_id + 1}",
                    "second_contact": {
                        "first_name": "Emily",
                        "last_name": "Brown",
                        "email": f"contact2_{unique_id}@novadigital.com",
                        "phone": f"+1-555-{unique_id + 2}",
                    },
                },
                "notes": {
                    "public_notes": "Premium support customer with yearly contract",
                    "private_notes": "Always pays invoices before due date",
                },
                "settings": {
                    "language": "English",
                    "invoice_payment_terms": "Due on Receipt",
                    "quote_valid_until": "Due on Receipt",
                    "send_reminders": "Disabled",
                    "custom_value": f"CUST-{unique_id}",
                    "size": "1 - 3",
                },
                "billing_address": {
                    "street": "789 Market Street",
                    "apt_suite": "Floor 12",
                    "city": "Chicago",
                    "state": "IL",
                    "postal_code": "60601",
                    "country": "United States",
                    "country_search": "United States",
                },
                "shipping_address": {
                    "street": "654 Warehouse Blvd",
                    "apt_suite": "Unit 8",
                    "city": "Houston",
                    "state": "TX",
                    "postal_code": "77001",
                    "country": "United States",
                    "country_search": "United States",
                },
            }
        ]
    }

    with open("data/client_data.json", "w") as json_file:
        json.dump(client_data, json_file, indent=2)

    print("\n========== NEW CLIENT TEST DATA GENERATED ==========\n")


# Generate fresh data before loading JSON
generate_client_data()


# Load test data
with open("data/client_data.json") as f:
    test_data = json.load(f)


@pytest.mark.order(2)
@allure.feature("Clients")
@pytest.mark.smoke
@allure.story("Create Client")
class TestClient:
    @allure.title("Create client and validate in database")
    @allure.description("Validate client creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("client", test_data["clients"])
    def test_create_client_and_db_validation(self, driver, db, client):

        print("\n========== CLIENT CREATION TEST STARTED ==========\n")
        print(f"[TEST DATA] {client}")

        client_page = ClientPage(driver)
        sidebar_page = SidebarPage(driver)

        # Step 0 - Close the popup
        # with allure.step("Side bar or Close or back initial popup"):
        #     sidebar_page.close_initial_popup()
        with allure.step("Side bar menu"):
            sidebar_page.open_sidebar()

        # Step 2 - Click Clients
        with allure.step("Open Clients section"):
            sidebar_page.open_clients()

        # Step 3 - Click New Client
        with allure.step("Click New Client"):
            print("[UI] Looking for New Client button")
            new_client = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "New Client")
            assert new_client.is_displayed(), "New Client button not visible"
            print("[UI] Clicking New Client")
            new_client.click()
            time.sleep(2)

        # ==================== CLIENT BASIC INFO ====================

        # Step 4 - Enter Client Name
        client_page.enter_client_name(client["name"])

        # Step 5 - Select New User
        client_page.select_new_user()

        # Step 6 - Enter ID Number
        client_page.enter_id_number(client["id_number"])

        # Step 7 - Enter VAT Number
        client_page.enter_vat_number(client["vat_number"])

        # Step 8 - Enter Website
        client_page.enter_website(client["website"])

        # Step 9 - Enter Phone Number
        client_page.enter_phone_number(client["phone"])

        # ==================== CONTACTS TAB ====================

        # Step 10 - Navigate to Contacts Tab
        client_page.navigate_to_contacts_tab()

        # Step 11 - Enter First Name
        client_page.enter_first_name(client["contacts"]["first_name"])

        # Step 12 - Enter Last Name
        client_page.enter_last_name(client["contacts"]["last_name"])

        # Step 13 - Enter Contact Email
        client_page.enter_contact_email(client["contacts"]["email"])

        # Step 14 - Enter Contact Phone
        client_page.enter_contact_phone(client["contacts"]["phone"])

        # Step 15 - Add Second Contact
        client_page.click_add_second_contact()

        # Step 16 - Enter Second Contact First Name
        client_page.enter_second_contact_first_name(
            client["contacts"]["second_contact"]["first_name"]
        )

        # Step 17 - Enter Second Contact Last Name
        client_page.enter_second_contact_last_name(
            client["contacts"]["second_contact"]["last_name"]
        )

        # Step 18 - Enter Second Contact Email
        client_page.enter_second_contact_email(
            client["contacts"]["second_contact"]["email"]
        )

        # Step 19 - Enter Second Contact Phone
        client_page.enter_second_contact_phone(
            client["contacts"]["second_contact"]["phone"]
        )

        # Step 20 - Click DONE
        client_page.click_done_button()

        # ==================== NOTES TAB ====================

        # Step 21 - Navigate to Notes Tab
        client_page.navigate_to_notes_tab()

        # Step 22 - Enter Public Notes
        client_page.enter_public_notes(client["notes"]["public_notes"])

        # Step 23 - Enter Private Notes
        client_page.enter_private_notes(client["notes"]["private_notes"])

        # ==================== SETTINGS TAB ====================

        # Step 24 - Navigate to Settings Tab
        client_page.navigate_to_settings_tab()

        # Step 25 - Select Language
        client_page.select_language(client["settings"]["language"])

        # Step 26 - Select Invoice Payment Terms
        client_page.select_invoice_payment_terms(
            client["settings"]["invoice_payment_terms"]
        )

        # Step 27 - Select Quote Valid Until
        client_page.select_quote_valid_until(client["settings"]["quote_valid_until"])

        # Step 28 - Select Send Reminders
        client_page.select_send_reminders(client["settings"]["send_reminders"])

        # Step 29 - Enter Custom Value
        client_page.enter_custom_value(client["settings"]["custom_value"])

        # Step 30 - Select Size
        client_page.select_size(client["settings"]["size"])

        # ==================== BILLING ADDRESS TAB ====================

        # Step 31 - Navigate to Billing Address Tab
        client_page.navigate_to_billing_address_tab()

        # Step 32 - Enter Billing Street
        client_page.enter_billing_street(client["billing_address"]["street"])

        # Step 33 - Enter Billing Apt/Suite
        client_page.enter_billing_apt_suite(client["billing_address"]["apt_suite"])

        # Step 34 - Enter Billing City
        client_page.enter_billing_city(client["billing_address"]["city"])

        # Step 35 - Enter Billing State
        client_page.enter_billing_state(client["billing_address"]["state"])

        # Step 36 - Enter Billing Postal Code
        client_page.enter_billing_postal_code(client["billing_address"]["postal_code"])

        # Step 37 - Select Billing Country
        client_page.select_billing_country(
            client["billing_address"]["country_search"],
            client["billing_address"]["country"],
        )

        # ==================== SHIPPING ADDRESS TAB ====================

        # Step 38 - Navigate to Shipping Address Tab
        client_page.navigate_to_shipping_address_tab()

        # Step 39 - Enter Shipping Street
        client_page.enter_shipping_street(client["shipping_address"]["street"])

        # Step 40 - Enter Shipping Apt/Suite
        client_page.enter_shipping_apt_suite(client["shipping_address"]["apt_suite"])

        # Step 41 - Enter Shipping City
        client_page.enter_shipping_city(client["shipping_address"]["city"])

        # Step 42 - Enter Shipping State
        client_page.enter_shipping_state(client["shipping_address"]["state"])

        # Step 43 - Enter Shipping Postal Code
        client_page.enter_shipping_postal_code(
            client["shipping_address"]["postal_code"]
        )

        # Step 44 - Select Shipping Country
        client_page.select_shipping_country(
            client["shipping_address"]["country_search"],
            client["shipping_address"]["country"],
        )

        # ==================== SAVE ====================

        # Step 45 - Click Save
        client_page.click_save_button()
        time.sleep(3)

        # TODO: Add DB validation here using the 'db' fixture
        # Example:
        # with allure.step("Validate client in database"):
        #     assert db.validate_client_exists(client["name"]), "Client not found in DB"
        # ==================== DATABASE VALIDATION ====================

        # Step 45 - Validate in Database
        with allure.step("Validate client in database"):
            print("\n========== DATABASE VALIDATION STARTED ==========\n")

            query = """
                    SELECT
                        c.id,
                        c.name,
                        c.id_number,
                        c.vat_number,
                        c.website,
                        c.phone,
                        c.public_notes,
                        c.private_notes,
                        c.address1              AS billing_street,
                        c.address2              AS billing_apt,
                        c.city                  AS billing_city,
                        c.state                 AS billing_state,
                        c.postal_code           AS billing_postal,
                        co.name                 AS billing_country,
                        c.shipping_address1     AS shipping_street,
                        c.shipping_address2     AS shipping_apt,
                        c.shipping_city         AS shipping_city,
                        c.shipping_state        AS shipping_state,
                        c.shipping_postal_code  AS shipping_postal,
                        sc.name                 AS shipping_country
                    FROM clients c
                             LEFT JOIN countries co ON co.id = c.country_id
                             LEFT JOIN countries sc ON sc.id = c.shipping_country_id
                    WHERE c.name = %s
                    ORDER BY c.id DESC
                        LIMIT 1 \
                    """

            params = (client["name"],)

            print(f"[DB] Executing Query:\n{query}")
            print(f"[DB] Query Parameters: {params}")

            result = db.fetch_one(query, params)

            print(f"[DB] Raw Query Result: {result}")

            assert (
                result is not None
            ), f"Client '{client['name']}' not found in database"

            # Core fields
            assert (
                result["name"] == client["name"]
            ), f"Name mismatch: expected '{client['name']}', got '{result['name']}'"

            assert (
                result["id_number"] == client["id_number"]
            ), f"ID Number mismatch: expected '{client['id_number']}', got '{result['id_number']}'"

            assert (
                result["vat_number"] == client["vat_number"]
            ), f"VAT Number mismatch: expected '{client['vat_number']}', got '{result['vat_number']}'"

            assert (
                result["website"] == client["website"]
            ), f"Website mismatch: expected '{client['website']}', got '{result['website']}'"

            assert (
                result["phone"] == client["phone"]
            ), f"Phone mismatch: expected '{client['phone']}', got '{result['phone']}'"

            # Notes
            assert (
                result["public_notes"] == client["notes"]["public_notes"]
            ), f"Public notes mismatch: expected '{client['notes']['public_notes']}', got '{result['public_notes']}'"

            assert (
                result["private_notes"] == client["notes"]["private_notes"]
            ), f"Private notes mismatch: expected '{client['notes']['private_notes']}', got '{result['private_notes']}'"

            # Billing address
            assert (
                result["billing_street"] == client["billing_address"]["street"]
            ), f"Billing street mismatch"

            assert (
                result["billing_city"] == client["billing_address"]["city"]
            ), f"Billing city mismatch"

            assert (
                result["billing_state"] == client["billing_address"]["state"]
            ), f"Billing state mismatch"

            assert (
                result["billing_postal"] == client["billing_address"]["postal_code"]
            ), f"Billing postal code mismatch"

            assert (
                result["billing_country"] == client["billing_address"]["country"]
            ), f"Billing country mismatch"

            # Shipping address
            assert (
                result["shipping_street"] == client["shipping_address"]["street"]
            ), f"Shipping street mismatch"

            assert (
                result["shipping_city"] == client["shipping_address"]["city"]
            ), f"Shipping city mismatch"

            assert (
                result["shipping_state"] == client["shipping_address"]["state"]
            ), f"Shipping state mismatch"

            assert (
                result["shipping_postal"] == client["shipping_address"]["postal_code"]
            ), f"Shipping postal code mismatch"

            assert (
                result["shipping_country"] == client["shipping_address"]["country"]
            ), f"Shipping country mismatch"

            print(f"[DB] Client ID: {result['id']}")
            print(f"[DB] All fields validated successfully")
            print("\n========== DATABASE VALIDATION COMPLETED ==========\n")

        print("========== CLIENT CREATION TEST COMPLETED ==========\n")
