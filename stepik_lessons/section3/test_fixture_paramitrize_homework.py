# Задание: параметризация тестов из пункта 3.6
import time, math, pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Пути для url
path_list = ["236895", "236896", "236897", "236898",
             "236899", "236903", "236904", "236905"]


def get_number():
    answer = math.log(int(time.time() + 0.2))
    return str(answer)


# Фикстура для запуска и закрытия браузера. Для каждой функции свой экземпляр
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")


# Установил маркеры для теста
@pytest.mark.regression
@pytest.mark.parametrize('path', path_list)
def test_message_search(browser, path):
    try:
        link = f'https://stepik.org/lesson/{path}/step/1'
        browser.get(link)
        wait = WebDriverWait(browser, 5)

        text_area = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "textarea[data-autogrow]"))
        )
        number = get_number()
        text_area.send_keys(number)
        button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        # # Можно найти сразу текст, если текст будет найден вернется True иначе False
        # answer = wait.until(EC.text_to_be_present_in_element(
        #     (By.CLASS_NAME, "smart-hints__hint"), "Correct!")
        # )
        # А можно сначала получить элемент, если он найден
        answer = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "smart-hints__hint"))
        )

        assert answer.text == "Correct!"#, 'Text is not like "Correct!"'
    finally:
        browser.quit()

