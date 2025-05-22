from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DriverFactory:
    @staticmethod
    def get_driver():
        logger.info("Initializing ChromeDriver...")
        service = Service(ChromeDriverManager().install())
        logger.info(f"ChromeDriver path: {service.path}")
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        logger.info("ChromeDriver initialized successfully")
        return driver