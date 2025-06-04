from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ItemDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.item_name = (By.CSS_SELECTOR, '.inventory_details_name')
        self.item_description = (By.CSS_SELECTOR, '.inventory_details_desc')
        self.item_price = (By.CSS_SELECTOR, '.inventory_details_price')
        self.add_to_cart_button = (By.XPATH, '//button[contains(@data-test, "add-to-cart")]')
        self.remove_button = (By.XPATH, '//button[contains(@data-test, "remove")]')
        self.back_button = (By.ID, 'back-to-products')
        self.cart_badge = (By.CSS_SELECTOR, '.shopping_cart_badge')

    def navigate_to_item(self, item_id=0):
        logger.info(f"Navigating to item details page for item ID: {item_id}")
        self.driver.get(f"https://www.saucedemo.com/inventory-item.html?id={item_id}")

    def ensure_page_loaded(self):
        logger.info("Ensuring item details page is loaded")
        self.wait.until(lambda d: d.current_url.endswith('/inventory-item.html'))
        self.wait.until(EC.presence_of_element_located(self.item_name))

    def get_item_name(self):
        self.ensure_page_loaded()
        name = self.wait.until(EC.visibility_of_element_located(self.item_name)).text
        logger.info(f"Item name: {name}")
        return name

    def get_item_description(self):
        self.ensure_page_loaded()
        description = self.wait.until(EC.visibility_of_element_located(self.item_description)).text
        logger.info(f"Item description: {description}")
        return description

    def get_item_price(self):
        self.ensure_page_loaded()
        price = self.wait.until(EC.visibility_of_element_located(self.item_price)).text
        price = float(price.replace('$', ''))
        logger.info(f"Item price: {price}")
        return price

    def add_to_cart(self):
        self.ensure_page_loaded()
        logger.info("Adding item to cart")
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_button)).click()

    def is_remove_button_displayed(self):
        self.ensure_page_loaded()
        button = self.wait.until(EC.visibility_of_element_located(self.remove_button))
        is_displayed = button.is_displayed()
        logger.info(f"Remove button displayed: {is_displayed}")
        return is_displayed

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

    def click_back_to_products(self):
        self.ensure_page_loaded()
        logger.info("Clicking back to products button")
        self.wait.until(EC.element_to_be_clickable(self.back_button)).click()