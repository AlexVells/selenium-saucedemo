import logging
import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

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
def cart_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart(index=0)
    cart_page = CartPage(driver)
    cart_page.navigate()
    return cart_page

@allure.feature("Cart Page")
@allure.story("Cart Display")
@allure.title("Test cart items count")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_items_count(cart_page):
    logger.info("Starting test_cart_items_count")
    with allure.step("Verify 1 item in cart"):
        assert cart_page.get_cart_items_count() == 1, "Expected 1 item in cart"
        logger.info("Test successful: 1 item in cart")

@allure.feature("Cart Page")
@allure.story("Cart Display")
@allure.title("Test cart item name")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_item_name(cart_page):
    logger.info("Starting test_cart_item_name")
    with allure.step("Verify cart item name"):
        item_names = cart_page.get_cart_item_names()
        assert len(item_names) == 1, "Expected 1 item in cart"
        assert item_names[0] == "Sauce Labs Backpack", "Expected item name to be 'Sauce Labs Backpack'"
        logger.info("Test successful: Cart item name verified")