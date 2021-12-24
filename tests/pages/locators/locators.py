from appium.webdriver.common.appiumby import AppiumBy

class ChromeLocators:
    CLOSE_TRANSLATION_FRAME = (AppiumBy.ID, "com.android.chrome:id/infobar_close_button")
    CONFIRM_CLOSING = (AppiumBy.ID, "com.android.chrome:id/infobar_close_button")

class MainPageLocators:
    CAR_SELL_PAGE = (AppiumBy.XPATH, "//div[@class='b-ab-layer']//a[contains(@class, 'btn-yellow')]")


class SellCarPageLocators:
    FILTER_BUTTON = (AppiumBy.XPATH, "//a[contains(@class, 'vehicle-form__button_filter')]")
    BRAND_TEXT_FORM = (AppiumBy.XPATH, "//div[contains(@class, 'dropdown-style_visible')]//input[@type='text' and @placeholder]")
    COUNTRY_FORM = (AppiumBy.XPATH, "(//div[contains(@class, 'input-style_arrow')])[1]")
    RADIO_BUTTON_BELARUS = (AppiumBy.XPATH, "//input[@value=248]/..")
    CAR_BRAND_FILTER = (AppiumBy.XPATH, "(//div[contains(@class, 'input-style_arrow')])[4]")
    MINI_BRAND_CHECKBOX = (AppiumBy.XPATH, "//input[@value='43']/..")
    CLOSE_CAR_FILTER_BUTTON = (AppiumBy.XPATH, "//div[contains(@class, 'vehicle-form__filter-toggle')]")
    CAR_LINK_NAMES = (AppiumBy.XPATH, "//div[contains(@class, 'vehicle-form__link_middle')]/ancestor::a[@href]")


class NavigationSidebarLocators:
    SIDE_SLIDEBAR = (AppiumBy.CLASS_NAME, "header-style__underlay")
    HOUSES_LINK = (AppiumBy.XPATH, "(//a[@href='#']/span[@class='header-style__sign'])[last()]")
    SELL_HOUSE_LINK = (AppiumBy.XPATH, "//ul/li[@class='header-style__item']/a[@href='https://r.onliner.by']")
    
class SellApartmentPageLocators:
    FILTER_ICON = (AppiumBy.XPATH, "//a[@data-control='filter']")
    AMOUNT_HOUSES_DESCRIPTION = (AppiumBy.XPATH, "//div[@class='mobile-bar-secondary__text']")
    
class FilterSellHouseBarLocators:
    MAX_PRICE_VALUE = (AppiumBy.XPATH, "//*[@id='search-filter-price-to']")
    MIN_PRICE_VALUE = (AppiumBy.XPATH, "//*[@id='search-filter-price-from']")
    STUDIO_APARTMENT_CHECKBOX = (AppiumBy.XPATH, "//span[@class='filter__item-inner' and contains(text(),'1')]")
    NEW_BUILDING_CHECKBOX = (AppiumBy.XPATH, "//span[@class='filter__item-inner' and contains(text(),'1')]")
    

    
    