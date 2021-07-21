from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    page_product = ProductPage(browser, link)
    page_product.open()

    page_product.basket_adding()
    page_product.should_be_message_about_adding_product()
    page_product.should_be_products_name_equal()
    page_product.should_be_prices_equal()

