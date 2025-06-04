from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.postal_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.finish_button = (By.ID, 'finish')
        self.cancel_button = (By.ID, 'cancel')
        self.checkout_complete_message = (By.CSS_SELECTOR, '.complete-header')
        self.cart_items = (By.CSS_SELECTOR, '.cart_item')

    def navigate_to_step_one(self):
        logger.info("Navigating to checkout step one")
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def ensure_page_loaded(self, step):
        logger.info(f"Ensuring checkout step {step} is loaded")
        if step == 1:
            self.wait.until(lambda d: d.current_url.endswith('/checkout-step-one.html'))
            self.wait.until(EC.presence_of_element_located(self.first_name_input))
        elif step == 2:
            self.wait.until(lambda d: d.current_url.endswith('/checkout-step-two.html'))
            self.wait.until(EC.presence_of_element_located(self.finish_button))
        elif step == "complete":
            self.wait.until(lambda d: d.current_url.endswith('/checkout-complete.html'))
            self.wait.until(EC.presence_of_element_located(self.checkout_complete_message))

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.ensure_page_loaded(1)
        logger.info(f"Filling checkout info: {first_name}, {last_name}, {postal_code}")
        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located(self.postal_code_input)).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def click_finish(self):
        self.ensure_page_loaded(2)
        logger.info("Clicking finish button")
        self.wait.until(EC.element_to_be_clickable(self.finish_button)).click()

    def click_cancel(self):
        self.ensure_page_loaded(2)
        logger.info("Clicking cancel button")
        self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()

    def get_checkout_complete_message(self):
        self.ensure_page_loaded("complete")
        message = self.wait.until(EC.visibility_of_element_located(self.checkout_complete_message)).text
        logger.info(f"Checkout complete message: {message}")
        return message

    def get_cart_items_count(self):
        self.ensure_page_loaded(2)
        items = self.wait.until(EC.visibility_of_all_elements_located(self.cart_items))
        logger.info(f"Found {len(items)} cart items")
        return len(items)