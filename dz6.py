'''
Маєте словник зі списком користувачів та їх віковими групами. Запитайте користувача про ім'я та виведіть вікову групу.
Врахуйте випадок, коли ім'я користувача не знайдено у словнику
'''


users = {
    "Tom": "junior",
    "Teja": "junior",
    "Emilis": "senior",
    "Guste": "senior",
    "Naglis": "average",
    "Ania": "average",
}

name = input("Please enter your name: ")

if name in users:
    age_group = users[name]
    print(f"Your age group: {age_group}")
else:
    print("Sorry, the name was not found in the dictionary.")
