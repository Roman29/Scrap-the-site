import requests
from bs4 import BeautifulSoup

URL = 'https://rozetka.com.ua/'
HEADERS = {
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'Accept-Ranges': 'bytes'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_text(html):
    soup = BeautifulSoup(html, 'html.scrapper')
    items = soup.find_all('div', class_='product-item')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='title').get_text(strip=True),
                'linc': item.find('div', class_='title').find('a').get('href'),
                'price': item.find('div', class_='brand').get_text(strip=True),

            }
        )
    return cards


def scrap():
    html = get_html(URL)
    if html.status_code == 200:
        print("status_code = ", html.status_code)


scrap()
