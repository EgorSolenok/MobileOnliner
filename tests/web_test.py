import pytest

from config import TEST_SUBJECT_URL
from tests.pages.main_page import MainPage
from tests.pages.sell_apartment_page import SellApartmentPage
from tests.pages.sell_car_page import SellCarPage


@pytest.fixture(scope='function', autouse=True)
def app(android_browser):
    yield
    android_browser.reset()

class TestGuestActions:
    
    def test_guest_can_go_to_sell_houses_and_should_see_correct_page(self, android_browser, app):
        main_page = MainPage(android_browser, TEST_SUBJECT_URL)
        main_page.open()
        main_page.go_to_side_slidebar()
        main_page.go_to_houses()
        main_page.go_to_sell_houses()
        apartment_page = SellApartmentPage(android_browser, android_browser.current_url)
        apartment_page.close_translation()
        apartment_page.should_be_amount_description()
        
    def test_guest_can_go_to_car_sell_page_and_should_see_correct_page(self, android_browser, app):
        main_page = MainPage(android_browser, TEST_SUBJECT_URL)
        main_page.open()
        main_page.close_translation()
        main_page.go_to_car_sell_page()
        car_page = SellCarPage(android_browser, android_browser.current_url)
        car_page.close_translation()
        car_page.go_to_filter()
        car_page.select_country()
        car_page.select_car_brand()
        car_page.close_car_filter()
        car_page.should_be_correct_car_brand()
        
    

        





"""
If i need to go search
mobile_web_driver.execute_script('mobile: performEditorAction', {'action': 'search'})
common actions include: go, search, send, next, done, previous
"""
"""
if i need to accept pop up 
pop_button = driver.find_element_by_class_name('android.widget.Button')
driver.set_value(pop_button, 'NOT NOW')
"""

