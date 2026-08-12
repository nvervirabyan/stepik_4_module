from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import BasketPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def basket_should_not_be_full(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_not_element_present(*BasketPageLocators.FULL_BASKET), "Basket is full"

    def basket_should_be_empty(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT), "Basket is not empty"
