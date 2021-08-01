import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                  ])
class TestClassProductPage:
    def test_guest_can_add_product_to_basket(self, browser, link):
        page_product = ProductPage(browser, link)
        page_product.open()

        page_product.basket_adding()
        page_product.should_be_message_about_adding_product()
        page_product.should_be_products_name_equal()
        page_product.should_be_prices_equal()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page_product = ProductPage(browser, link)
        page_product.open()
        page_product.basket_adding()
        page_product.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, link):
        page_product = ProductPage(browser, link)
        page_product.open()
        page_product.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page_product = ProductPage(browser, link)
        page_product.open()
        page_product.basket_adding()
        page_product.should_be_is_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_that_basket_is_empty()  # Переписать, сделать унивирсальную проверку

