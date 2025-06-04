import logging
import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

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
def checkout_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart(index=0)
    cart_page = CartPage(driver)
    cart_page.navigate()
    checkout_page = CheckoutPage(driver)
    checkout_page.navigate_to_step_one()
    return checkout_page

@allure.feature("Checkout Page")
@allure.story("Checkout Step One")
@allure.title("Test filling checkout information")
@allure.severity(allure.severity_level.NORMAL)
def test_fill_checkout_info(checkout_page):
    logger.info("Starting test_fill_checkout_info")
    with allure.step("Fill checkout information"):
        checkout_page.fill_checkout_info("John", "Doe", "12345")
    with allure.step("Verify navigation to step two"):
        checkout_page.ensure_page_loaded(2)
        assert "checkout-step-two" in checkout_page.driver.current_url, "Did not navigate to step two"
        logger.info("Test successful: Checkout info filled and navigated to step two")

@allure.feature("Checkout Page")
@allure.story("Checkout Step Two")
@allure.title("Test completing checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_complete_checkout(checkout_page):
    logger.info("Starting test_complete_checkout")
    with allure.step("Fill checkout information"):
        checkout_page.fill_checkout_info("John", "Doe", "12345")
    with allure.step("Click finish button"):
        checkout_page.click_finish()
    with allure.step("Verify checkout completion"):
        checkout_page.ensure_page_loaded("complete")
        message = checkout_page.get_checkout_complete_message()
        assert "Thank you" in message, "Checkout not completed successfully"
        logger.info("Test successful: Checkout completed")

@allure.feature("Checkout Page")
@allure.story("Checkout Step Two")
@allure.title("Test canceling checkout")
@allure.severity(allure.severity_level.NORMAL)
def test_cancel_checkout(checkout_page):
    logger.info("Starting test_cancel_checkout")
    with allure.step("Fill checkout information"):
        checkout_page.fill_checkout_info("John", "Doe", "12345")
    with allure.step("Click cancel button"):
        checkout_page.click_cancel()
    with allure.step("Verify navigation to inventory page"):
        assert "inventory" in checkout_page.driver.current_url, "Did not navigate back to inventory page"
        logger.info("Test successful: Checkout canceled and navigated back to inventory")