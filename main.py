import requests
from bs4 import BeautifulSoup as Bs
import time

url_page = 'https://cars.av.by/filter'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


class Parser:
    def __init__(self, pages: range, headers):
        self.pages = pages
        self.url = 'https://cars.av.by/filter'
        self.get_html()

    def get_html(self):
        for page in self.pages:
            if page != 1:
                self.url = f'https://cars.av.by/filter?page={page}'
            responce = requests.get(self.url, headers=headers)
            self._get_info(responce, page)

    def _get_info(self, html_source, page_num: int):
        print(f'Страница номер : {page_num}\n')
        soup = Bs(html_source.text, 'lxml')
        data = soup.find_all('a', class_='listing-item__link')
        price = soup.find_all('div', class_='listing-item__prices')
        info = soup.find_all('div', class_='listing-item__params')
        link = soup.find_all('a', class_='listing-item__link')

        for i in range(len(data)):
            print(data[i].find('span', class_='link-text').text, ' | ', price[i].find('div', class_='listing-item__price').text,
                  ' | ', info[i].text, ' | ', html_source.url.split('filter')[0]+link[i].get('href'))
        print()


if __name__=='__main__':
    parser = Parser(range(1, 10), headers)

