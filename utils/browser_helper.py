import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BrowserHelper():
    @allure.step("Find visible element by '{1}', '{2}' for max - '{timeout}' seconds")
    def find_clickable_element(browser, how, what, timeout=8):
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        return required_element
    
    def find_visible_element(browser, how, what, timeout=4):
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.visibility_of_element_located((how, what)))
        return required_element
    
    def find_visible_elements(browser, how, what, timeout=4):
        required_elements = WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located((how, what)))
        return required_elements
