'''

"""
>>> 2+2
5
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()


import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="Some text - %(asctime)s:%(levelname)s: %(message)s")

try:
    print(10/0)
except Exception:
    logging.exception("Exception")

logging.debug("debug")
logging.info("info")



age = int(input("Enter your age "))
if age < 100:
    print(f"Your age is {age}")
    logging.info("correct")
else:
    print("You enter bad age")
    logging.info("incorrect")


logging.warning("warning")
logging.error("error")
logging.critical("critical")


assert 2+2 == 5, "incorrect"
'''


#zd1
#Створіть програму, яка використовує модуль logging для запису повідомлення рівня "INFO" із поточною датою у форматі
# "Рік-Місяць-День"


import logging
import datetime
logging.basicConfig(level=logging.INFO, filename="date.log", filemode="w")
date = datetime.datetime.now().strftime("%Y-%m-%d")
logging.info("Date: %s", date)

'''

#zd2
#Створіть програму, яка використовує обробник помилок. Використайте модуль logging для запису повідомлень рівня "ERROR" 
# разом із текстом винятку.
'''



