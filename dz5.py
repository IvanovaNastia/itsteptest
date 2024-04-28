import colorama

print(dir(colorama))


important = [
    "AnsiToWin32", "Back", "Fore", "Style", "init", "deinit", "ansi", "win32"
]

for item in important:
    if hasattr(colorama, item):
        print(f"{item}: {getattr(colorama, item)}")

'''
Що робить кожин з виокремлених атрибутів та методів:
1. AnsiToWin32: Цей клас використовується для перетворення ANSI-кодів кольорів у відповідні кольори в системі Windows.
2. Back, Fore і Style: Ці атрибути надають доступ до колекцій кольорів та стилів тексту. Наприклад, Back.BLUE зробить 
синій фон, Fore.RED дасть червоний колір тексту, а Style.BRIGHT зробить текст яскравішим
3. init і deinit: Ці методи використовуються для ініціалізації та деініціалізації бібліотеки colorama. init потрібно 
викликати перед використанням будь-яких функцій colorama, а deinit - для очищення ресурсів після завершення роботи з 
бібліотекою.
4. ansi і win32: Ці атрибути надають доступ до об'єктів, які працюють з ANSI- та Win32-системами відповідно.
'''
