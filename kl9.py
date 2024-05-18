"""
import urllib.request
opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())

////////////////////////////////////////////////

import requests
#get -- получить инфу
response = requests.get("https://httpbin.org/get")
print(response.text)
print(f"Datetype - {type(response.text)}")

#post - дать инфу

response = requests.post("https://httpbin.org/post", data="test data", headers={"h1": "Text title"})
print(response.text)

////////////////////////////

import requests

res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)


bitcoin = res_parse_list[0]
print(bitcoin)

//////////////////////////////////////////////
"""



#Завдання 1: Витягніть назви всіх книг зі сайту http://books.toscrape.com

from bs4 import BeautifulSoup
import requests

respone = requests.get("http://books.toscrape.com/")

if respone.status_code == 200:
    soup = BeautifulSoup(respone.text, features="html.parser")
    books = soup.find_all("h3")
    book_titles = [book.a['title'] for book in books]

for title in book_titles:
    print(title)
