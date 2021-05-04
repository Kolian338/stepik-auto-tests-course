from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control first"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control second"]')
    input2.send_keys("Petrov")
    input2 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control third"]')
    input2.send_keys("ivan.petrov@gmail.com")
    input3 = browser.find_element_by_xpath('//div[@class="second_block"]//input[@class="form-control first"]')
    input3.send_keys("68920")
    input4 = browser.find_element_by_xpath('//div[@class="second_block"]//input[@class="form-control second"]')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
