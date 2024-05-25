"""
#зав1
print("Завдання №1")
name = input("Вкажіть ваше ім'я: ")
old = input("Вкажіть ваш вік: ")
print("Привіт, " + name + " " + "тобі" + " " + old + "!")


#зав2
print("Завдання №2")
old1 = int(input("Вкажіть ваш вік: "))
if old1 >= 18:
    print("Вхід дозволено!")
elif old1 < 18:
    print("Вхід заборонено!")


#зав3
print("Завдання №3")
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
print("Завдання №4")
st = int(input("Введіть перше число (з): "))
end = int(input("Введіть друге число (по): "))

print("Числа від", st, "до", end, ":")
for st in range(st, end+1):
    if st > 0:
        print(st)


#зав5
print("Завдання №5")
num = int(input("Введіть значення n: "))

print("Парні числа від 1 до", num, "у зворотньому порядку:")
for x in range(num):
    if not x % 2:
        print(num - x)


#зав6
print("Завдання №6")
n = int(input("Ведіть число яке хочете найти в факторіалі: "))
fact = 1
for x in range(2, n+1):
    fact *= x
print(fact)


#зав7
print("Завдання №7")
a = int(input("Напишіть вашу оцінку: "))
if a <= 49:
    print("Ваша оцінка незадовільно")
elif 50 <= a <= 69:
    print("Ваша оцінка задовільно")
elif 70 <= a <= 89:
    print("Ваша оцінка добре")
else:
    print("Ваша оцінка відмінно")


#зав8
print("Завдання №8")
a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))
d = input("Введіть операцію (+, -, *, /): ")
if d == "+":
    print(a+b)
elif d == "-":
    print(a-b)
elif d == "*":
    print(a*b)
elif d == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print(a/b)
"""
