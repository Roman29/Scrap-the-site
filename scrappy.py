import csv
from bs4 import BeautifulSoup
from selenium import webdriver

CSV = 'phones.csv'
chromedriver = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
url = driver.get("https://rozetka.com.ua/")
driver.fullscreen_window()
driver.implicitly_wait(2)
phones_and_tv = driver.find_element_by_xpath(
    '/html/body/app-root/div/div[1]/app-rz-main-page/div/aside/main-page-sidebar/sidebar-fat-menu/div/ul/li[2]/a').click()
driver.implicitly_wait(1)
smartphones = driver.find_element_by_xpath(
    '/html/body/app-root/div/div[1]/app-rz-header/header/div/div[2]/div[1]/fat-menu/div/ul/li[2]/div/div[2]/div[1]/div[1]/ul[1]/li/ul/li[1]/a').click()
driver.implicitly_wait(1)
select_apple = driver.find_element_by_xpath(
    '/html/body/app-root/div/div[1]/rz-category/div/main/rz-catalog/div/div[2]/aside/rz-filter-stack/div[3]/div/rz-scrollbar/div/div[1]/div/div/rz-filter-section-checkbox/ul[1]/li[1]').click()
driver.implicitly_wait(1)
next_button = driver.find_element_by_class_name('show-more').click()

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
all_phones = soup.find_all(class_='goods-tile__inner')

try:
    with open("all_phones.csv", "w",newline='', encoding='utf8') as file:
        all_phone_file = csv.writer(file, delimiter=';')
        all_phones_dict = {}
        for item in all_phones:
            item_text = item.find(class_='goods-tile__title').contents[1].replace(u'Офіційна гарантія', '').replace(
                u'Мобільний телефон', '')
            item_price = item.find(class_='goods-tile__price-value').string.replace(u' ', '')
            item_href = item.find(class_='goods-tile__heading').attrs['href']
            print(f"{item_text}: {item_price}: {item_href}")
            all_phone_file.writerow([item_text, item_price, item_href])

except Exception as e:
    print('\n' * 2, "=====" * 10, "СOMPLETED", "=====" * 10)
driver.quit()
