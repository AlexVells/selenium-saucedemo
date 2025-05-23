from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DriverFactory:
    @staticmethod
    def get_driver():
        logger.info("Initializing ChromeDriver...")
        service = Service("C:\\Program Files\\ChromeDriver\\chromedriver.exe")
        logger.info(f"ChromeDriver path: {service.path}")
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        logger.info("ChromeDriver initialized successfully")
        return driver