import allure

from tests.pages.base_page import BasePage
from tests.pages.locators.locators import FilterSellHouseBarLocators
from tests.pages.locators.locators import SellApartmentPageLocators
from utils.browser_helper import BrowserHelper

class SellApartmentPage(BasePage):
    @allure.step("Set minimum and maximum prices")
    def set_prices(self):
        BrowserHelper.send_keys(self.android_browser, *FilterSellHouseBarLocators.MIN_PRICE_VALUE, '10000')
        BrowserHelper.send_keys(self.android_browser, *FilterSellHouseBarLocators.MAX_PRICE_VALUE, '50000')
        
    @allure.step("Set studio type")
    def set_studio(self):
        BrowserHelper.click_element(self.android_browser, *FilterSellHouseBarLocators.STUDIO_APARTMENT_CHECKBOX)
        
    @allure.step("Set new building")
    def set_new_building(self):
        BrowserHelper.click_element(self.android_browser, *FilterSellHouseBarLocators.NEW_BUILDING_CHECKBOX)

    @allure.step("Verification of description with amount of available houses")
    def should_be_amount_description(self):
        amount_description = BrowserHelper.find_visible_element(self.android_browser, *SellApartmentPageLocators.AMOUNT_HOUSES_DESCRIPTION)
        assert amount_description, "There is no description with amount of variants"
        
    
    