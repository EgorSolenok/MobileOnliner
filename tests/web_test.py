import allure

from config import TEST_SUBJECT_URL
from tests.pages.main_page import MainPage
from tests.pages.sell_apartment_page import SellApartmentPage
from tests.pages.sell_car_page import SellCarPage


@allure.feature("Guest actions from main page")
@allure.severity("critical")
class TestGuestActions:
    @allure.story("Guest can should see correct sell house title")
    @allure.severity("critical")
    def test_guest_should_see_correct_sell_house_title(self, android_browser):
        main_page = MainPage(android_browser, TEST_SUBJECT_URL)
        main_page.open()
        main_page.go_to_house_sell_page()
        apartment_page = SellApartmentPage(android_browser, android_browser.current_url)
        apartment_page.close_translation()
        apartment_page.should_be_amount_description()
    
    
    @allure.story("Guest should see correct car brands to sell")
    @allure.severity("critical")
    def test_guest_should_see_correct_car_brands_to_sell(self, android_browser):
        main_page = MainPage(android_browser, TEST_SUBJECT_URL)
        main_page.open()
        main_page.close_translation()
        main_page.go_to_car_sell_page()
        car_page = SellCarPage(android_browser, android_browser.current_url)
        car_page.close_translation()
        car_page.select_country()
        car_page.select_car_brand()
        car_page.should_be_correct_car_brand()
