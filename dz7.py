#Реалізувати генератор, який видає послідовність випадкових букв алфавіту.

import random
import string

def random_letter():
    while True:
        yield random.choice(string.ascii_lowercase)

generator = random_letter()

for _ in range(26):
    print(next(generator))