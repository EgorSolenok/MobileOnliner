import pytest
from utils.server_logger import create_logs_file
from appium import webdriver
from config import WEB_CAPABILITIES
from config import APPIUM_HOST, APPIUM_PORT


@pytest.fixture(scope='session')
def android_browser():
    android_browser = webdriver.Remote(
        command_executor=f"http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub",
        desired_capabilities=WEB_CAPABILITIES
    )
    yield android_browser
    
    create_logs_file(android_browser)
    android_browser.quit()