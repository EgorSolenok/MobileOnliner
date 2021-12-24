from datetime import datetime


APPIUM_PORT = '4723'
APPIUM_HOST = 'localhost'

TEST_SUBJECT_URL = "https://onliner.by/"

WEB_CAPABILITIES = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "browserName": "Chrome",
}

FILE_LOG_NAME = (str(datetime.now())[2:16]).replace(':',' ')

