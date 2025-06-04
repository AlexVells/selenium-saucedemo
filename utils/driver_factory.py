from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DriverFactory:
    @staticmethod
    def get_driver():
        logger.info("Initializing ChromeDriver...")
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        chrome_options.add_argument("--disable-infobars")
        
        service = Service("C:\\Program Files\\ChromeDriver\\chromedriver.exe")
        logger.info(f"ChromeDriver path: {service.path}")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        logger.info("ChromeDriver initialized successfully")
        return driver