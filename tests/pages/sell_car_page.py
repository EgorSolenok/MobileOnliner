import allure

from tests.pages.base_page import BasePage
from tests.pages.locators.locators import SellCarPageLocators
from utils.browser_helper import BrowserHelper


class SellCarPage(BasePage):
    @allure.step("Select required country")
    def select_country(self):
        BrowserHelper.click_element(self.android_browser, *SellCarPageLocators.FILTER_BUTTON)
        BrowserHelper.click_element(self.android_browser, *SellCarPageLocators.COUNTRY_FORM)
        BrowserHelper.click_element(self.android_browser, *SellCarPageLocators.RADIO_BUTTON_BELARUS)


    @allure.step("Select required car brand")
    def select_car_brand(self):
        BrowserHelper.click_element(self.android_browser, *SellCarPageLocators.CAR_BRAND_FILTER)
        BrowserHelper.send_keys(self.android_browser, *SellCarPageLocators.BRAND_TEXT_FORM, 'mini')
        BrowserHelper.click_element(self.android_browser, *SellCarPageLocators.MINI_BRAND_CHECKBOX)
        BrowserHelper.click_element(self.android_browser, *SellCarPageLocators.CLOSE_CAR_FILTER_BUTTON)
    
    
    @allure.step("Verification of brand names in links of car cards")
    def should_be_correct_car_brand(self):
        car_names = BrowserHelper.find_visible_elements(self.android_browser, *SellCarPageLocators.CAR_LINK_NAMES)
        for car_name in car_names:
            assert 'mini' in car_name.get_attribute("href"), "There is incorrect car name in description"
