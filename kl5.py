#zav1
'''
try:
    name = input("Вкажіть ваше ім'я: ")
    age = input("Вкажіть ваш вік: ")
    print("Привіт, " + name + " " + "тобі" + " " + age + "!")

except:
    print("eroor")
else:
    print("no errors")
#zav2

try:
    age = int(input("Вкажіть ваш вік: "))
    if age >= 18:
        print("Вхід дозволено!")
    else:
        print("Вхід заборонено!")
except:
    print("eroor")
else:
    print("no errors")

#zav3
import random
try:
    secret_number = random.randint(1, 10)
    tr = 3
    print("Привіт! Це гра 'Вгадай число'. Я загадав число від 1 до 10. У вас 3 спроби")
    while tr > 0:
        print("У вас залишилося", tr, "спроби(а).")
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
            print(f"Вітаю! Ви вгадали число {secret_number}!")
            break
        elif guess < secret_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")

        tr -= 1

    if tr == 0:
        print(f"На жаль, спроби закінчилися. Загадане число було: {secret_number}.")

except:
    print("eroor")
else:
    print("no errors")

#zav4
try:
    st = int(input("Введіть перше число (з): "))
    end = int(input("Введіть друге число (по): "))
    print("Числа від", st, "до", end, ":")
    for st in range(st, end+1):
        if st > 0:
            print(st)

except:
    print("eroor")
else:
    print("no errors")

#zav5
try:
    num = int(input("Введіть значення n: "))

    print("Парні числа від 1 до", num, "у зворотньому порядку:")
    for x in range(num):
        if not x % 2:
            print(num - x)

except:
    print("eroor")
else:
    print("no errors")

#zav6
try:
    n = int(input("Ведіть число яке хочете найти в факторіалі: "))
    fact = 1
    for x in range(2, n + 1):
        fact *= x
    print(fact)

except:
    print("eroor")
else:
    print("no errors")

#zav7

try:
    a = int(input("Напишіть вашу оцінку: "))
    if a <= 49:
        print("Ваша оцінка незадовільно")
    elif 50 <= a <= 69:
        print("Ваша оцінка задовільно")
    elif 70 <= a <= 89:
        print("Ваша оцінка добре")
    else:
        print("Ваша оцінка відмінно")
except:
    print("eroor")
else:
    print("no errors")

    '''
#zav8
try:
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

except:
    print("Eroor")
else:
    print("No errors")