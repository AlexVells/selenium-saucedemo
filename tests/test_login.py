import logging
import pytest
import allure
from allure_commons.types import AttachmentType
from pages.login_page import LoginPage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('test_results.log')
    ]
)
logger = logging.getLogger(__name__)

@allure.feature("Login Page Elements")
@allure.story("Element Visibility")
@allure.title("Test username field visibility")
@allure.severity(allure.severity_level.NORMAL)
def test_username_field_is_visible(login_page):
    logger.info("Starting test_username_field_is_visible")
    with allure.step("Navigate to login page"):
        login_page.navigate()
    with allure.step("Verify username field is visible"):
        assert login_page.is_element_visible(login_page.username_input), "Username field is not shown"
        logger.info("Test successful: Username field is shown")

@allure.feature("Login Page Elements")
@allure.story("Element Visibility")
@allure.title("Test password field visibility")
@allure.severity(allure.severity_level.NORMAL)
def test_password_field_is_visible(login_page):
    logger.info("Starting test_password_field_is_visible")
    with allure.step("Navigate to login page"):
        login_page.navigate()
    with allure.step("Verify password field is visible"):
        assert login_page.is_element_visible(login_page.password_input), "Password field is not shown"
        logger.info("Test successful: Password field is shown")

@allure.feature("Login Page Elements")
@allure.story("Element Visibility")
@allure.title("Test login button visibility")
@allure.severity(allure.severity_level.NORMAL)
def test_login_button_is_visible(login_page):
    logger.info("Starting test_login_button_is_visible")
    with allure.step("Navigate to login page"):
        login_page.navigate()
    with allure.step("Verify login button is visible"):
        assert login_page.is_element_visible(login_page.login_button), "Login button is not shown"
        logger.info("Test successful: Login button is shown")

@allure.feature("Login Functionality")
@allure.story("Login Scenarios")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("standard_user", "secret_sauce", None),
        ("invalid_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")
    ]
)
@allure.title("Test login with {username}/{password}")
def test_login(login_page, username, password, expected_message):
    logger.info(f"Starting test_login with username: {username}, password: {password}")
    with allure.step("Navigate to login page"):
        login_page.navigate()
    with allure.step(f"Perform login with username: {username}, password: {password}"):
        login_page.login(username, password)
    
    if expected_message is None:
        with allure.step("Verify successful login"):
            assert login_page.is_login_successful(), "Login failed"
            logger.info("Test successful: User logged in")
    else:
        with allure.step("Verify error message"):
            error_message = login_page.get_error_message()
            assert error_message is not None, "Error message not displayed"
            assert expected_message in error_message, f"Unexpected error message: {error_message}"
            logger.info(f"Test successful: Error message displayed — '{error_message}'")

    