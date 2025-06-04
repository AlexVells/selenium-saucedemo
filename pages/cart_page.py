from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.cart_items = (By.CSS_SELECTOR, '.cart_item')
        self.checkout_button = (By.ID, 'checkout')
        self.cart_item_names = (By.CSS_SELECTOR, '.inventory_item_name')
    
    def navigate(self):
        logger.info("Navigating to cart page")
        self.driver.get("https://www.saucedemo.com/cart.html")
    
    def ensure_page_loaded(self):
        logger.info("Ensuring cart page is loaded")
        self.wait.until(lambda d: d.current_url.endswith('/cart.html'))
        self.wait.until(EC.presence_of_element_located(self.cart_items))

    def get_cart_items_count(self):
        self.ensure_page_loaded()
        items = self.wait.until(EC.visibility_of_all_elements_located(self.cart_items))
        logger.info(f"Found {len(items)} cart items")
        return len(items)
    
    def get_cart_item_names(self):
        self.ensure_page_loaded()
        items = self.wait.until(EC.visibility_of_all_elements_located(self.cart_item_names))
        names = [item.text for item in items]
        logger.info(f"Cart item names: {names}")
        return names
    
    def click_checkout(self):
        self.ensure_page_loaded()
        logger.info("Clicking checkout button")
        button = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        button.click()