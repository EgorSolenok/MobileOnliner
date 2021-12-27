import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BrowserHelper():
    @allure.step("Find clickable element by '{1}', '{2}'")
    def find_clickable_element(browser, how, what, timeout=5):
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        return required_element
    
    @allure.step("Click at element by '{1}', '{2}'")
    def click_element(browser, how, what, timeout=5):
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        required_element.click()

    @allure.step("Find visible element by '{1}', '{2}'")
    def find_visible_element(browser, how, what, timeout=5):
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.visibility_of_element_located((how, what)))
        return required_element
    
    @allure.step("Find visible elements by '{1}', '{2}'")
    def find_visible_elements(browser, how, what, timeout=5):
        required_elements = WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located((how, what)))
        return required_elements
    
    @allure.step("Send to '{1}', '{2}' values - '{3}'")
    def send_keys(browser, how, what, value, timeout=5, clear_first=True, click_first=True):
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        if click_first:
            required_element.click()
        if clear_first:
            required_element.clear()
        required_element.send_keys(value)