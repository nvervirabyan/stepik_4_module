from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLocators

class ProductPage(BasePage):
    # def should_be_product_url(self):
    #     # реализуйте проверку на корректный url адрес
    #     assert "?promo=newYear" in self.browser.current_url, "Promo in product page is not presented"

    # def add_product_to_basket(self):
    #     self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    # def should_be_product_added_to_basket(self):
    #     assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text, "Product on page and product added are different"

    # def should_be_basket_total_equal_product_price(self):
    #    assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text, "Price of product on page and basket total are different"

    # def is_not_element_present_on_page(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #    "Success message is presented, but should not be"

    # def is_disappeared_from_page(self):
    #     assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
    #     "Success message is not disappeares, but should be"

    def basket_should_not_be_full(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_not_element_present(*BasketPageLocators.FULL_BASKET), "Basket is full"

    def basket_should_be_empty(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT), "Basket is not empty"
