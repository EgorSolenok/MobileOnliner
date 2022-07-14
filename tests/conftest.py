import pytest
import allure
import os
from utils.server_logger import ServerLogger
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
    
    ServerLogger.get_logs(android_browser)
    android_browser.quit()
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

