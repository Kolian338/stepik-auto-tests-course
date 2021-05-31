import time, math, pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_list = ['236895', '236896', '236897', '236898',
             '236899', '236903', '236904', '236905']


def get_number():
    answer = math.log(int(time.time() + 0.2))
    return answer


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")


@pytest.mark.parametrize('path', "path_list")
def test_message_search(browser, path):
    try:
        link = f'https://stepik.org/lesson/{path}/step/1'
        browser.get(link)
        wait = WebDriverWait(browser, 5)
        number = get_number()
        text_area = wait.until(EC.element_to_be_clickable(By.ID, "ember89"))
        text_area.send_keys(number)
        button = wait.until(EC.element_to_be_clickable(By.CLASS_NAME, "submit-submission"))
        button.click()
        answer = wait.until(EC.text_to_be_present_in_element(By.CLASS_NAME, 'smart-hints__hint'), 'Correct!')

        assert answer.text == "Correct!", 'Text is not like "Correct!"'
    finally:
        browser.quit()