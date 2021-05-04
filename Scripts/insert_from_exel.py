import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#Указываем путь к файлу
book = openpyxl.open(r"C:\Users\Kolia\Downloads\date.xlsx", read_only=True)
#Указываем лист в экселе
sheet = book.active
#Строки(с 1)/Столбцы(от 0)
#print(sheet[1][0])

rowsCount = sheet.max_row + 1
columsCount = sheet.max_column + 1


id_list = []
category_list = []
type_list = []
name_list = []
short_name_list = []
mo_list = []
addres_list = []
corp_list = []
coordinate_list = []
state_list = []
responsible_list = []
phone_list = []
comment_list = []

link = "http://bg-back-testdevelop-sev.k8.sccloud.ru/login"
browser = webdriver.Chrome()
browser.maximize_window()

#Формируем список id записей объектов
#Проходим по строкам, берем значения в каждом столбце
for row in range(2, rowsCount):
    id_list.append(sheet[row][0].value)
    category_list.append(sheet[row][1].value)
    type_list.append(sheet[row][2].value)
    name_list.append(sheet[row][3].value)
    short_name_list.append(sheet[row][4].value)
    mo_list.append(sheet[row][5].value)
    state_list.append(sheet[row][9].value)
    phone_list.append(sheet[row][11].value)

try:
    browser.get(link)
    browser.implicitly_wait(4)
    input_login = browser.find_element_by_id("mat-input-0")
    input_login.send_keys("admin")
    input_password = browser.find_element_by_id("mat-input-1")
    input_password.send_keys("admin")
    button_submit = browser.find_element_by_css_selector('[type="submit"]')
    browser.implicitly_wait(4)
    button_submit.click()
    time.sleep(3)
    browser.get("http://bg-back-testdevelop-sev.k8.sccloud.ru/dictionaries/significant-objects")
    browser.implicitly_wait(4)

    button_plus = browser.find_element_by_css_selector(".grid-table__bar.bar div:nth-child(4) sc-button:nth-child(3)"
                                                       " > button")
    button_plus.click()

    time.sleep(2)
    category_input = browser.find_element_by_xpath('//*[@id="cdk-accordion-child-12"]/div/div[1]/div[1]/div/sc-select/'
                                                   'ng-select/div/div/div[2]/input')
    type_input = browser.find_element_by_xpath('//*[@id="cdk-accordion-child-12"]/div/div[1]/div[2]/div/sc-select/'
                                               'ng-select/div/div/div[2]/input')
    name_input = browser.find_element_by_css_selector('input[data-placeholder="Наименование"]')
    short_name_input = browser.find_element_by_css_selector('input[data-placeholder="Краткое наименование"]')
    mo_input = browser.find_element_by_xpath('//*[@id="cdk-accordion-child-12"]/div/div[4]/div/div/sc-select/'
                                             'ng-select/div/div/div[2]/input')
    addres_input = browser.find_element_by_id("mat-input-0")
    corp_input = browser.find_element_by_id("mat-input-3")
    coordinate_input = browser.find_element_by_id("mat-input-4")
    state_input = browser.find_element_by_xpath('//*[@id="cdk-accordion-child-12"]/div/div[7]/div[2]/div/sc-select/'
                                                'ng-select/div/div/div[2]/input')
    responsible = browser.find_element_by_id("mat-input-5")
    phone_input = browser.find_element_by_id("mat-input-6")
    comment_input = browser.find_element_by_id("mat-input-8")
    button_save = browser.find_element_by_css_selector(".bar .bar__actions .bar__action > button")
    button_update = browser.find_element_by_xpath('/html/body/app-root/app-layout/div/mat-sidenav-container/mat-sidenav-content/div/bg-layout/dictionaries-layout/significant-objects-layout/layout/div/div/layout-element/grid-table/mat-card/div/div[4]/sc-button[1]/button')

    for value in range(2):
        category_input.send_keys(category_list[value])
        select_category = browser.find_element_by_css_selector('div.ng-dropdown-panel-items.scroll-host .ng-option:nth-child(1)').click()

        name_input.send_keys(name_list[value])
        short_name_input.send_keys(short_name_list[value])

        mo_input.send_keys(mo_list[value])
        select_mo = browser.find_element_by_css_selector('div.ng-dropdown-panel-items.scroll-host .ng-option:nth-child(1)').click()

        state_input.send_keys(state_list[value])
        select_input = browser.find_element_by_css_selector('div.ng-dropdown-panel-items.scroll-host .ng-option:nth-child(1)').click()

        phone_input.send_keys(phone_list[value])
        button_save.click()
        button_update.click()
        time.sleep(2)
        button_plus.click()
        time.sleep(2)

finally:
    browser.quit()