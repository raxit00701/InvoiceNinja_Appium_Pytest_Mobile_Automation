import pytest
import allure
import json
import time
import random

from pages.product import ProductPage
from pages.sidebar import SidebarPage

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------------------------------------------------
# Load Test Data
# ---------------------------------------------------------

with open("data/product_data.json") as f:
    test_data = json.load(f)

unique_id = random.randint(1000, 9999)

product_data = {
    "product": [
        {
            "product_name": f"iphone xl pro {unique_id}",
            "description": "this is a phone that is build by apple",
            "price": 1899,
            "default_quantity": 30,
            "max_quantity": 310,
            "image_url": "https://apple.com/images/industrial-cargo-pallet.jpg",
        }
    ]
}


@pytest.mark.order(3)
@allure.feature("Products")
@allure.story("Create Product")
class TestClient:

    @allure.title("Create product and validate in database")
    @allure.description("Validate product creation flow and database validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("product", product_data["product"])
    def test_create_product_and_db_validation(self, driver, db, product):

        print("\n========== PRODUCT CREATION TEST STARTED ==========")

        print(f"\n[TEST DATA] {product}")

        wait = WebDriverWait(driver, 20)

        product_page = ProductPage(driver)
        sidebar_page = SidebarPage(driver)

        # ---------------------------------------------------------
        # Step 0 - Close popup if displayed
        # ---------------------------------------------------------

        with allure.step("Side bar or Close or back initial popup"):

            sidebar_page.click_back_button()
            sidebar_page.open_sidebar()

        # ---------------------------------------------------------
        # Step 1 - Open Products
        # ---------------------------------------------------------

        with allure.step("Click on Products"):

            print("\n[STEP] Opening Products")

            sidebar_page.click_products()

        # ---------------------------------------------------------
        # Step 2 - Click New Product
        # ---------------------------------------------------------

        with allure.step("Click on New Product"):

            print("[STEP] Clicking New Product")

            product_page.click_new_product()

        # ---------------------------------------------------------
        # Step 3 - Enter Product Name
        # ---------------------------------------------------------

        with allure.step("Enter Product Name"):

            print(f"[STEP] Enter Product Name: " f"{product['product_name']}")

            product_page.enter_product_name(product["product_name"])

        # ---------------------------------------------------------
        # Step 4 - Enter Description
        # ---------------------------------------------------------

        with allure.step("Enter Description"):

            print("[STEP] Enter Description")

            product_page.enter_description(product["description"])

        # ---------------------------------------------------------
        # Step 5 - Enter Price
        # ---------------------------------------------------------

        with allure.step("Enter Price"):

            print(f"[STEP] Enter Price: {product['price']}")

            product_page.enter_price(product["price"])

        # ---------------------------------------------------------
        # Step 6 - Enter Default Quantity
        # ---------------------------------------------------------

        with allure.step("Enter Default Quantity"):

            print(f"[STEP] Enter Default Quantity: " f"{product['default_quantity']}")

            product_page.enter_default_quantity(product["default_quantity"])

        # ---------------------------------------------------------
        # Step 7 - Enter Max Quantity
        # ---------------------------------------------------------

        with allure.step("Enter Max Quantity"):

            print(f"[STEP] Enter Max Quantity: " f"{product['max_quantity']}")

            product_page.enter_max_quantity(product["max_quantity"])

        # ---------------------------------------------------------
        # Step 8 - Enter Image URL
        # ---------------------------------------------------------

        with allure.step("Enter Image URL"):

            print("[STEP] Enter Image URL")

            product_page.enter_image_url(product["image_url"])

        # ---------------------------------------------------------
        # Step 9 - Click Save
        # ---------------------------------------------------------

        with allure.step("Tap Save"):

            print("[STEP] Clicking Save")

            product_page.click_save()
            time.sleep(5)

        # ---------------------------------------------------------
        # Step 10 - Verify Product Saved
        # ---------------------------------------------------------

        with allure.step("Verify Product Saved"):

            print("[VERIFY] Waiting for Product " "Overview Screen")

            wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Edit"))
            )

            print("[VERIFY] Product Created Successfully")

            # ==================== DATABASE VALIDATION ====================

        with allure.step("Validate Product In Database"):

            print("\n========== DATABASE VALIDATION " "STARTED ==========\n")

            query = """
                    SELECT
                        id,
                        product_key AS product_name,
                        notes AS description,
                        price,
                        quantity AS default_quantity,
                        max_quantity,
                        product_image AS image_url,
                        created_at
                    FROM products
                    WHERE TRIM(product_key) = TRIM(%s)
                      AND is_deleted = 0
                    ORDER BY created_at DESC
                        LIMIT 1
                    """

            params = (product["product_name"],)

            print(f"[DB] Executing Query:\n{query}")
            print(f"[DB] Query Parameters: {params}")

            result = None

            # ---------------------------------------------------------
            # Retry DB Fetch
            # ---------------------------------------------------------

            for attempt in range(15):

                print(f"\n[DB CHECK ATTEMPT {attempt + 1}]")

                try:

                    result = db.fetch_one(query, params)

                    print(f"[DB] Raw Query Result: {result}")

                    if result is not None:

                        print("[DB] Product found in database")

                        break

                except Exception as e:

                    print(f"[DB ERROR] {e}")

                print("[DB] Product not found yet. " "Waiting 3 seconds...")

                time.sleep(3)

            # ---------------------------------------------------------
            # Validate Record Exists
            # ---------------------------------------------------------

            assert result is not None, (
                f"Product '{product['product_name']}' " f"not found in database"
            )

            # ---------------------------------------------------------
            # Product Validation
            # ---------------------------------------------------------

            assert result["product_name"] == product["product_name"], (
                f"Product Name mismatch: expected "
                f"'{product['product_name']}', "
                f"got '{result['product_name']}'"
            )

            assert result["description"] == product["description"], (
                f"Description mismatch: expected "
                f"'{product['description']}', "
                f"got '{result['description']}'"
            )

            assert float(result["price"]) == float(product["price"]), (
                f"Price mismatch: expected "
                f"'{product['price']}', "
                f"got '{result['price']}'"
            )

            assert int(float(result["default_quantity"])) == int(
                product["default_quantity"]
            ), (
                f"Default Quantity mismatch: expected "
                f"'{product['default_quantity']}', "
                f"got '{result['default_quantity']}'"
            )

            assert int(result["max_quantity"]) == int(product["max_quantity"]), (
                f"Max Quantity mismatch: expected "
                f"'{product['max_quantity']}', "
                f"got '{result['max_quantity']}'"
            )

            assert result["image_url"] == product["image_url"], (
                f"Image URL mismatch: expected "
                f"'{product['image_url']}', "
                f"got '{result['image_url']}'"
            )

            # ---------------------------------------------------------
            # Print DB Values
            # ---------------------------------------------------------

            print("\n========== DATABASE VALUES ==========\n")

            print(f"Product ID       : {result['id']}")
            print(f"Product Name     : " f"{result['product_name']}")
            print(f"Description      : " f"{result['description']}")
            print(f"Price            : " f"{result['price']}")
            print(f"Default Quantity : " f"{result['default_quantity']}")
            print(f"Max Quantity     : " f"{result['max_quantity']}")
            print(f"Image URL        : " f"{result['image_url']}")
            print(f"Created At       : " f"{result['created_at']}")

            print("\n========== DATABASE VALIDATION " "COMPLETED ==========\n")
