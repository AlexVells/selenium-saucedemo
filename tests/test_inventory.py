import logging
import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

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
def inventory_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(driver)

@allure.feature("Inventory Page")
@allure.story("Item Display")
@allure.title("Test inventory items count")
@allure.severity(allure.severity_level.NORMAL)
def test_inventory_items_count(inventory_page):
    logger.info("Starting test_inventory_items_count")
    with allure.step("Verify 6 items are displayed"):
        assert inventory_page.get_inventory_items_count() == 6, "Expected 6 items in inventory"
        logger.info("Test successful: 6 items displayed")

@allure.feature("Inventory Page")
@allure.story("Sorting")
@allure.title("Test inventory sorting")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "sort_option, expected_order_type",
    [
        ("az", "asc_names"),  
        ("za", "desc_names"),  
        ("lohi", "asc_prices"),  
        ("hilo", "desc_prices") 
    ]
)
def test_inventory_sorting(inventory_page, sort_option, expected_order_type):
    logger.info(f"Starting test_inventory_sorting with option: {sort_option}")
    with allure.step(f"Select sort option: {sort_option}"):
        inventory_page.select_sort_option(sort_option)
    with allure.step("Verify items are sorted correctly"):
        if "names" in expected_order_type:
            items = inventory_page.get_inventory_items_names()
            expected_items = sorted(items) if "asc" in expected_order_type else sorted(items, reverse=True)
            assert items == expected_items, f"Items not sorted correctly for {sort_option}: {items} vs {expected_items}"
        else:
            prices = inventory_page.get_inventory_items_prices()
            expected_prices = sorted(prices) if "asc" in expected_order_type else sorted(prices, reverse=True)
            assert prices == expected_prices, f"Prices not sorted correctly for {sort_option}: {prices} vs {expected_prices}"
        logger.info(f"Test successful: Items sorted correctly for {sort_option}")

@allure.feature("Inventory Page")
@allure.story("Cart Functionality")
@allure.title("Test add item to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart(inventory_page):
    logger.info("Starting test_add_item_to_cart")
    with allure.step("Add first item to cart"):
        inventory_page.add_item_to_cart(index=0)
    with allure.step("Verify Remove button is displayed"):
        assert inventory_page.is_remove_button_displayed(index=0), "Remove button not displayed"
    with allure.step("Verify cart badge shows 1 item"):
        assert inventory_page.get_cart_item_count() == 1, "Cart badge does not show 1 item"
        logger.info("Test successful: Item added to cart")