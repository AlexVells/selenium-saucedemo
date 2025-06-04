from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.CSS_SELECTOR, 'input[data-test="username"]')
        self.password_input = (By.CSS_SELECTOR, 'input[data-test="password"]')
        self.login_button = (By.CSS_SELECTOR, 'input[data-test="login-button"]')
        self.inventory_list = (By.CSS_SELECTOR, '.inventory_list')
        self.error_message = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def navigate(self):
        self.driver.get(self.url)

    def is_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.inventory_list))
            return True
        except:
            return False

    def get_error_message(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            return element.text
        except:
            return None