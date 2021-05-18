from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    wait = WebDriverWait(browser, 12)
    # Ждет пока появится ожидаемый текст у элемента в настоящее время
    price_text = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button_book = browser.find_element_by_id('book').click()

    number = browser.find_element_by_id('input_value').text
    result = calc(number)
    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_css_selector("[type='submit']").click()

    alert = browser.switch_to_alert().text

    print(alert.split(':')[1])
finally:
    browser.quit()