
'''
#зав1
name = input("Вкажіть ваше ім'я: ")
old = input("Вкажіть ваш вік: ")
print("Привіт, " + name + " " + "тобі" + " " + old + "!")

#зав2
old1 = int(input("Вкажіть ваш вік: "))
if old1 >= 18:
    print("Вхід дозволено!")
elif old1 < 18:
    print("Вхід заборонено!")

#зав3
import random

secret_number = random.randint(1, 10)
tr = 3

print("Привіт! Це гра 'Вгадай число'. Я загадав число від 1 до 10. У вас 3 спроби")

while tr > 0:
    print("У вас залишилося",  tr, "спроби(а).")
    guess = input("Введіть вашу догадку: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        continue

    if guess < 1 or guess > 10:
        print("Будь ласка, введіть число від 1 до 10.")
        continue

    if guess == secret_number:
        print("Вітаю! Ви вгадали число {secret_number}!")
        break
    elif guess < secret_number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")

    tr -= 1

if tr == 0:
    print("На жаль, спроби закінчилися. Загадане число було: {secret_number}.")

#зав4

try:
    st = int(input("Введіть перше число (з): "))
    end = int(input("Введіть друге число (по): "))
except ValueError:
    print("Будь ласка, введіть цілі числа.")
    re

if st > end:
    print("Перше число повинно бути менше або рівне другого числа.")


print("Числа від {start} до {end}:")
for num in range(st, end + 1):
    print(num)
'''
class Human:
    def __init__(self):
        self.height = 175


denis = Human()
print(denis.height)