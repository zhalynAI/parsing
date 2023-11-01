import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='browse-view')
    laptops = catalog.find_all('div', class_='row')
    # laptop = catalog.find('div', class_='row')
    for laptop in laptops:
        title = laptop.find('a',
        class_='product-image-link').get('title')
        image = laptop.find('img').get('src')
        image = f'https://enter.kg/{image}'
        price = laptop.find('span', class_='price').text
                
        data = {
            'title':title,
            'image':image,
            'price':price

        }

        write_csv(data)

def write_csv(data):
    with open('enter_laptops.csv', 'a') as csv_file:
        names = ['title', 'price', 'image']
        writer = csv.DictWriter(csv_file, delimiter='|', fieldnames=names)
        writer.writerow(data)

response = get_html('https://enter.kg/computers/noutbuki_bishkek')
get_data(response)

def main():
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(url)
    get_data(html)

main()
f'https://enter.kg/computers/noutbuki_bishkek/results{101}-{100}'

def get_last_name(html):
    """
    это функция находит ссылку на последнюю страницу
    """
    soup = BS(html, 'lxml')
    url_last_page = soup.find('li', print())

def main():
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(url)
    # last_page = get_last_page(html)
    # get_data(html)