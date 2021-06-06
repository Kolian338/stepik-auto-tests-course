import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест для проверки кнопки добавления товара, на различных языках. Использовать в CLI параметр --language=en
def test_check_basket_button_exists(browser):
    try:
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        wait = WebDriverWait(browser, 5)
        button_basket = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button.btn-add-to-basket'))
        )
        # time.sleep(5)
        assert button_basket
    except:
        raise
