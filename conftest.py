import pytest
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def login_page():
    driver = DriverFactory.get_driver()
    login_page = LoginPage(driver)
    yield login_page
    driver.quit()