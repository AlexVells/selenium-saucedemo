import pytest
import allure
from allure_commons.types import AttachmentType
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver, request):
    login_page = LoginPage(driver)
    yield login_page
    if hasattr(request.node, "callspec") and request.node.session.testsfailed > 0:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"screenshot_{request.node.name}",
            attachment_type=AttachmentType.PNG
        )