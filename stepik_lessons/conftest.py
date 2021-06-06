import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Обработчик опции при запуске pytest. Установка опций происходит из фикстуры browser
def pytest_addoption(parser):
    print('Start parser')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


# Фикстура которая будет обрабатывать переданные в опции данные
@pytest.fixture(scope="function")
def browser(request):
    # Для Chrome
    # Передаем в заголовках язык браузера (Пример параметра: --language=es)
    options = Options()
    print('\ngetting settings from CLI')
    user_language = request.config.getoption("language")
    print('\nadd settings to header')
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # Для firefox
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)

    # Запускаем браузер который мы указали в консоли, в параметрах (Пример параметра: --browser_name=chrome)
    browser_name = request.config.getoption("browser_name")
    browser = None  # На что это влияет ?
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()