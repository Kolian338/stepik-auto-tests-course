import unittest
from selenium import webdriver


class TestRegistration(unittest.TestCase):
    def test_page1_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)
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

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected_result = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_result, "Не удалось зарегистрироваться, фактический результат: "
                                                        f"{welcome_text}, ожидаемый результат: {expected_result}")

    def test_page2_registration(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)
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

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected_result = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_result, "Не удалось зарегистрироваться, фактический результат: "
                                                        f"{welcome_text}, ожидаемый результат: {expected_result}")


if __name__ == "__main__":
    unittest.main()
