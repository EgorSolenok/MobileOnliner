from tests.pages.base_page import BasePage
from tests.pages.locators.locators import NavigationSidebarLocators
from tests.pages.locators.locators import MainPageLocators
from utils.browser_helper import BrowserHelper

class MainPage(BasePage):
    def go_to_side_slidebar(self):
        side_slidebar = BrowserHelper.find_clickable_element(self.android_browser, *NavigationSidebarLocators.SIDE_SLIDEBAR)
        side_slidebar.click()
        
    def go_to_houses(self):
        houses_dropdown = BrowserHelper.find_clickable_element(self.android_browser, *NavigationSidebarLocators.HOUSES_LINK)
        houses_dropdown.click()
        
    def go_to_sell_houses(self):
        sell_link = BrowserHelper.find_clickable_element(self.android_browser, *NavigationSidebarLocators.SELL_HOUSE_LINK)
        sell_link.click()
        
    def go_to_car_sell_page(self):
        car_sell_link = BrowserHelper.find_clickable_element(self.android_browser, *MainPageLocators.CAR_SELL_PAGE)
        car_sell_link.click()
        
        
        