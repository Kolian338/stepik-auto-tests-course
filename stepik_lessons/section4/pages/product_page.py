from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Добавление товара в корзину
    def basket_adding(self):
        basket_button_add = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON_ADD)
        basket_button_add.click()

        # Найти и решить уравнение, получить код
    def solve_quiz_and_get_code(self):
        BasePage.solve_quiz_and_get_code(self)  # Алерт с кодом

        # Проверяем что есть сообщение о добавлении товара в корзину
    def should_be_message_about_adding_product(self):
        self.is_element_present(*ProductPageLocators.PRODUCT_ADDING_IN_MESSAGE), 'no message about adding'

        # Проверяем что нет сообщения о добавлении товара в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDING_IN_MESSAGE), \
            "Success message is presented, but should not be"

        # Ждем пока элемент не исчезнет
    def should_be_is_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDING_IN_MESSAGE), \
            "item has not disappeared"

        # Названия продуктов одинаковые, в сообщении и на странице
    def should_be_products_name_equal(self):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDING_IN_MESSAGE).text
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        assert product_name_on_page == product_name_in_message, 'Product names are different'

        # Проверяем равенство цен товара на странице и в сообщении
    def should_be_prices_equal(self):
        basket_price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_MESSAGE).text
        product_price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert basket_price_in_message == product_price_on_page, 'prices differ'




