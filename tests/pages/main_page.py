import allure

from tests.pages.base_page import BasePage
from tests.pages.locators.locators import NavigationSidebarLocators
from tests.pages.locators.locators import MainPageLocators
from utils.browser_helper import BrowserHelper


class MainPage(BasePage):
    @allure.step("Going to page with selling houses through slidebar")
    def go_to_house_sell_page(self):
        BrowserHelper.click_element(self.android_browser, *NavigationSidebarLocators.SIDE_SLIDEBAR)
        BrowserHelper.click_element(self.android_browser, *NavigationSidebarLocators.HOUSES_LINK)
        BrowserHelper.click_element(self.android_browser, *NavigationSidebarLocators.SELL_HOUSE_LINK)
    
    @allure.step("Going to page with selling car from main page")
    def go_to_car_sell_page(self):
        BrowserHelper.click_element(self.android_browser, *MainPageLocators.CAR_SELL_PAGE)
