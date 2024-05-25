import requests
from bs4 import BeautifulSoup
from collections import defaultdict

class DB:
    def __init__(self):
        self.links = []

    def add_link(self, link):
        self.links.append(link)

    def clear_links(self):
        self.links = []

    def get_links(self):
        return self.links

class SParser:
    def fetch_content(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return ""
        except requests.RequestException:
            return ""

    def count_occurrences(self, content, search_term):
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text().lower()
        return text.count(search_term.lower())

class Interface:
    def __init__(self, db_handler, parser):
        self.db_handler = db_handler
        self.parser = parser

    def add_site(self):
        link = input("Введіть URL, щоб додати: ")
        self.db_handler.add_link(link)

    def clear_sites(self):
        self.db_handler.clear_links()
        print("Базу даних очищено.")

    def search(self):
        term = input("Введіть пошуковий термін: ")
        links = self.db_handler.get_links()
        results = defaultdict(int)

        for link in links:
            content = self.parser.fetch_content(link)
            if content:
                count = self.parser.count_occurrences(content, term)
                results[link] = count

        sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
        for link, count in sorted_results:
            print(f"{link}: {count} збіги")

def run():
    db_handler = DB()
    parser = SParser()
    ui = Interface(db_handler, parser)

    while True:
        print("\n1. Додати сайт")
        print("2. Очистити сайти")
        print("3. Пошук")
        print("4. Вихід")
        choice = input("Виберіть дію: ")

        if choice == '1':
            ui.add_site()
        elif choice == '2':
            ui.clear_sites()
        elif choice == '3':
            ui.search()
        elif choice == '4':
            break
        else:
            print("Недійсний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    run()
