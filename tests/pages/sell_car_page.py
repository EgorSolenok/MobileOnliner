from tests.pages.base_page import BasePage
from tests.pages.locators.locators import SellCarPageLocators
from utils.browser_helper import BrowserHelper


class SellCarPage(BasePage):
    
    def go_to_filter(self):
        filter_button = BrowserHelper.find_visible_element(self.android_browser, *SellCarPageLocators.FILTER_BUTTON)
        filter_button.click()
    
    def select_country(self):
        country_form = BrowserHelper.find_visible_element(self.android_browser, *SellCarPageLocators.COUNTRY_FORM)
        country_form.click()
        belarus_button = BrowserHelper.find_visible_element(self.android_browser,
                                                            *SellCarPageLocators.RADIO_BUTTON_BELARUS)
        belarus_button.click()
    
    def select_car_brand(self):
        brand_filter = BrowserHelper.find_visible_element(self.android_browser, *SellCarPageLocators.CAR_BRAND_FILTER)
        brand_filter.click()
        car_text_form = BrowserHelper.find_visible_element(self.android_browser, *SellCarPageLocators.BRAND_TEXT_FORM)
        car_text_form.send_keys('mini')
        mini_brand_checkbox = BrowserHelper.find_visible_element(self.android_browser,
                                                                 *SellCarPageLocators.MINI_BRAND_CHECKBOX)
        mini_brand_checkbox.click()
    
    def close_car_filter(self):
        close_button = BrowserHelper.find_visible_element(self.android_browser,
                                                          *SellCarPageLocators.CLOSE_CAR_FILTER_BUTTON)
        close_button.click()
    
    def should_be_correct_car_brand(self):
        car_names = BrowserHelper.find_visible_elements(self.android_browser, *SellCarPageLocators.CAR_LINK_NAMES)
        for car_name in car_names:
            assert 'mini' in car_name.get_attribute("href"), "There is incorrect car name in description"
