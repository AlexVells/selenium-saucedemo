import logging
import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.item_details_page import ItemDetailsPage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('test_results.log')
    ]
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def item_details_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    item_details_page = ItemDetailsPage(driver)
    item_details_page.navigate_to_item(item_id=0) 
    return item_details_page

@allure.feature("Item Details Page")
@allure.story("Item Display")
@allure.title("Test item details display")
@allure.severity(allure.severity_level.NORMAL)
def test_item_details_display(item_details_page):
    logger.info("Starting test_item_details_display")
    with allure.step("Verify item name"):
        name = item_details_page.get_item_name()
        assert name == "Sauce Labs Backpack", "Item name does not match expected"
    with allure.step("Verify item description"):
        description = item_details_page.get_item_description()
        assert description, "Item description should not be empty"
    with allure.step("Verify item price"):
        price = item_details_page.get_item_price()
        assert price == 29.99, "Item price does not match expected"
        logger.info("Test successful: Item details displayed correctly")

@allure.feature("Item Details Page")
@allure.story("Cart Functionality")
@allure.title("Test add item to cart from details page")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart(item_details_page):
    logger.info("Starting test_add_item_to_cart")
    with allure.step("Add item to cart"):
        item_details_page.add_to_cart()
    with allure.step("Verify Remove button is displayed"):
        assert item_details_page.is_remove_button_displayed(), "Remove button not displayed"
    with allure.step("Verify cart badge shows 1 item"):
        assert item_details_page.get_cart_item_count() == 1, "Cart badge does not show 1 item"
        logger.info("Test successful: Item added to cart from details page")

@allure.feature("Item Details Page")
@allure.story("Navigation")
@allure.title("Test back to products navigation")
@allure.severity(allure.severity_level.NORMAL)
def test_back_to_products(item_details_page):
    logger.info("Starting test_back_to_products")
    with allure.step("Click back to products button"):
        item_details_page.click_back_to_products()
    with allure.step("Verify navigation to inventory page"):
        assert "inventory.html" in item_details_page.driver.current_url, "Did not navigate back to inventory page"
        logger.info("Test successful: Navigated back to inventory page")