from tests.pages.locators.locators import ChromeLocators
from utils.browser_helper import BrowserHelper


class BasePage:
    def __init__(self, android_browser, url):
        self.android_browser = android_browser
        self.url = url
        
    def open(self):
        self.android_browser.get(self.url)
        
    def __switch_to_web_context(self):
        webview = self.android_browser.contexts[1]
        self.android_browser.switch_to.context(webview)
        
    def close_translation(self):
        native = self.android_browser.contexts[0]
        self.android_browser.switch_to.context(native)
        decline_button = BrowserHelper.find_visible_element(
            self.android_browser, *ChromeLocators.CLOSE_TRANSLATION_FRAME)
        decline_button.click()
        try:
            confirm_button = BrowserHelper.find_visible_element(
                self.android_browser, *ChromeLocators.CONFIRM_CLOSING, timeout=4)
            confirm_button.click()
        except:
            pass
        self.__switch_to_web_context()