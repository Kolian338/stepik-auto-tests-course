link = "http://selenium1py.pythonanywhere.com/"


# В этом примере будем использовать плагин для перезапуска тестов
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
