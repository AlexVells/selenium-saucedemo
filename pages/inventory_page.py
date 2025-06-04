from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.inventory_items = (By.CSS_SELECTOR, '.inventory_item')
        self.sort_dropdown = (By.CSS_SELECTOR, 'select.product_sort_container')
        self.add_to_cart_button = (By.XPATH, '//button[contains(@data-test, "add-to-cart")]')
        self.remove_button = (By.XPATH, '//button[contains(@data-test, "remove")]')
        self.cart_badge = (By.CSS_SELECTOR, '.shopping_cart_badge')
        self.inventory_item_names = (By.CSS_SELECTOR, '.inventory_item_name')
        self.inventory_item_prices = (By.CSS_SELECTOR, '.inventory_item_price')

    def ensure_page_loaded(self):
        """Ensure the inventory page is fully loaded."""
        logger.info("Ensuring inventory page is loaded")
        self.wait.until(lambda d: d.current_url.endswith('/inventory.html'))
        self.wait.until(EC.presence_of_element_located(self.inventory_items))

    def get_inventory_items_count(self):
        self.ensure_page_loaded()
        items = self.wait.until(EC.visibility_of_all_elements_located(self.inventory_items))
        logger.info(f"Found {len(items)} inventory items")
        return len(items)
    
    def select_sort_option(self, option_value):
        """Select sort option from dropdown (e.g., 'az', 'za', 'lohi', 'hilo')."""
        self.ensure_page_loaded()
        logger.info(f"Selecting sort option: {option_value}")
        dropdown = self.wait.until(EC.visibility_of_element_located(self.sort_dropdown))
        dropdown = self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))
        dropdown.click()
        option = (By.CSS_SELECTOR, f'option[value="{option_value}"]')
        self.wait.until(EC.element_to_be_clickable(option)).click()
    
    def get_inventory_items_names(self):
        self.ensure_page_loaded()
        items = self.wait.until(EC.visibility_of_all_elements_located(self.inventory_item_names))
        names = [item.text for item in items]
        logger.info(f"Item names: {names}")
        return names
    
    def get_inventory_items_prices(self):
        self.ensure_page_loaded()
        prices = self.wait.until(EC.visibility_of_all_elements_located(self.inventory_item_prices))
        prices = [float(price.text.replace('$', '')) for price in prices]
        logger.info(f"Item prices: {prices}")
        return prices
    
    def add_item_to_cart(self, index=0):
        self.ensure_page_loaded()
        logger.info(f"Adding item {index} to cart")
        buttons = self.wait.until(EC.visibility_of_all_elements_located(self.add_to_cart_button))
        buttons[index].click()
    
    def get_cart_item_count(self):
        self.ensure_page_loaded()
        try:
            badge = self.wait.until(EC.visibility_of_element_located(self.cart_badge))
            count = int(badge.text)
            logger.info(f"Cart item count: {count}")
            return count
        except:
            logger.info("No items in cart")
            return 0
    
    def is_remove_button_displayed(self, index=0):
        self.ensure_page_loaded()
        buttons = self.wait.until(EC.visibility_of_all_elements_located(self.remove_button))
        is_displayed = buttons[index].is_displayed()
        logger.info(f"Remove button displayed for item {index}: {is_displayed}")
        return is_displayed