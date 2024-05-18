#Витягніть ціну кожної книги зі сайту http://books.toscrape.com

#Витягніть назви всіх книг зі сайту http://books.toscrape.com
'''
from bs4 import BeautifulSoup
import requests

respone = requests.get("http://books.toscrape.com/")

if respone.status_code == 200:
    soup = BeautifulSoup(respone.text, features="html.parser")
    books = soup.find_all("h3")
    book_titles = [book.a['title'] for book in books]

for title in book_titles:
    print(title)

/////////////////////////////////////////////////
'''

import requests
from bs4 import BeautifulSoup

respone = 'http://books.toscrape.com/catalogue/page-{}.html'


def extract_books_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    books = soup.find_all(class_='product_pod')

    book_list = []
    for book in books:
        title = book.h3.a['title']
        price = book.find(class_='price_color').get_text()
        book_list.append((title, price))

    return book_list

def extract_all_books():
    page_number = 1
    all_books = []

    while True:
        url = respone.format(page_number)
        response = requests.get(url)

        if response.status_code != 200:
            break

        page_books = extract_books_from_page(url)
        all_books.extend(page_books)

        print(f'Зібрано {len(page_books)} книг з сторінки {page_number}')

        page_number += 1

    return all_books

all_books = extract_all_books()
print(f'Всього книг зібрано: {len(all_books)}')
for title, price in all_books:
    print(f'{title}: {price}')