from tests.pages.base_page import BasePage
from tests.pages.locators.locators import FilterSellHouseBarLocators
from tests.pages.locators.locators import SellApartmentPageLocators
from utils.browser_helper import BrowserHelper

class SellApartmentPage(BasePage):
    def set_minimum_price(self):
        minimum_price = BrowserHelper.find_visible_element(self.android_browser, *FilterSellHouseBarLocators.MIN_PRICE_VALUE)
        minimum_price.send_keys('1')
        
    def set_maximum_price(self):
        maximum_price = BrowserHelper.find_visible_element(self.android_browser, *FilterSellHouseBarLocators.MAX_PRICE_VALUE)
        maximum_price.send_keys('12')
    
    def set_studio(self):
        studio_button = BrowserHelper.find_visible_element(self.android_browser, *FilterSellHouseBarLocators.STUDIO_APARTMENT_CHECKBOX)
        studio_button.click()
        
    def set_new_building(self):
        new_building_checkbox = BrowserHelper.find_visible_element(self.android_browser, *FilterSellHouseBarLocators.NEW_BUILDING_CHECKBOX)
        new_building_checkbox.click()
        
    def should_be_amount_description(self):
        amount_description = BrowserHelper.find_visible_element(self.android_browser, *SellApartmentPageLocators.AMOUNT_HOUSES_DESCRIPTION)
        assert amount_description, "There is no description with amount of variants"
        
    
    