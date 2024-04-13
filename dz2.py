#зав2
class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


toyota = Car(1982, "Toyota", "Camry")
bmw = Car(2018, "BMW", "X5")
mercedes = Car(1997, "Mercedes-Benz", "GLE")
audi = Car(2010, "Audi", "A1")
nissan = Car(2015, "Nissan", "Fuga")
porsche = Car(2013, "Porsche", "Cayenne")
print("Інформація про автомобіль: ", toyota)
print("Інформація про автомобіль: ", bmw)
print("Інформація про автомобіль: ", mercedes)
print("Інформація про автомобіль: ", audi)
print("Інформація про автомобіль: ", nissan)
print("Інформація про автомобіль: ", porsche)


#зав3
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Заробітна плата {self.name}: {self.salary}"

ania = Employee("Ані", "менеджер", "175000 грн")
oksana = Employee("Оксани", "продавець", "155000 грн")
max = Employee("Максима", "продавець", "155000 грн")
egor = Employee("Егора", "менеджер", "175000 грн")
lena = Employee("Лени", "продавець", "155000 грн")
print(ania)
print(oksana)
print(max)
print(egor)
print(lena)


#зав4
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)



rectangle = Rectangle(15, 25)
area = rectangle.calculate_area()
print(area)
perimeter = rectangle.calculate_perimeter()
print(perimeter)


#зав5
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return f"{self.quantity * self.price}"

    def display_info(self):
        return f"{self.name} {self.price} {self.quantity}"



aplle = Product("Яблоко", 7, 50)
totalpr1 = aplle.calculate_total_price()
print(totalpr1)
info1 = aplle.display_info()
print(info1)

banana = Product("Банан", 5, 47)
totalpr2 = banana.calculate_total_price()
print(totalpr2)
info2 = banana.display_info()
print(info2)

orange = Product("Апельсин", 10, 34)
totalpr3 = orange.calculate_total_price()
print(totalpr3)
info3 = orange.display_info()
print(info3)

mandarin = Product("Мандарин", 10, 37)
totalpr4 = mandarin.calculate_total_price()
print(totalpr4)
info4 = mandarin.display_info()
print(info4)

strawberry = Product("Полуниця", 13, 50)
totalpr5 = strawberry.calculate_total_price()
print(totalpr5)
info5 = strawberry.display_info()
print(info5)

