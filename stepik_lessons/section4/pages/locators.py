from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # Специально не верный локатор


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_BUTTON_ADD = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_ADDING_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) strong')
    BASKET_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')






