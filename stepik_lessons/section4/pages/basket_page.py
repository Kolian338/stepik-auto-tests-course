from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_not_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_text_about_that_basket_is_empty(self):
        text_basket_empty = self.browser.find_element(*BasketPageLocators.TEXT_THAT_BASKET_IS_EMPTY).text.split(".")[0]
        assert text_basket_empty == "Your basket is empty"
