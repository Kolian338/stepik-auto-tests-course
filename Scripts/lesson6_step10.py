from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".first[required]")
    input2 = browser.find_element_by_css_selector(".second[required]")
    input3 = browser.find_element_by_css_selector(".third[required]")
    input1.send_keys("TestText1")
    input2.send_keys("TestText2")
    input3.send_keys("TestText3")

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name('[type="submit"]')
    button.click()

    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    expected_result = "Congratulations! You have successfully registered!"
    assert expected_result == welcome_text
finally:
    browser.quit()


