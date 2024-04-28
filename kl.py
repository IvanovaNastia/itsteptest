'''
#kl 2
class Human:
    def __init__(self, name = "Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Name of {self.brand} passengers:")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"There are no passenhers in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")

car = Auto("Mercedes")

car.add_passengers(nick)
car.add_passengers(kate)

car.print_passengers_names()

#kl3

class Human:
    height = 150
    age = 15
    name = "Den"
    weight = 100

class Student(Human):
    weight = 60

class Pupil(Human):
    weight = 40


den = Student()
kate = Pupil()

print(den.weight, den.age)
print(kate.weight, kate.age)


///////////////////////////////////////////////

class Class1:
    war = 20
    def __init__(self):
        self.war = 10


class Class2(Class1):
    def __init__(self):
        print(self.war)
        super().__init__()
        print(self.war)
        print(super().war)

hellow = Class2()

////////////////////////////////////////////////////

class Computer:
    def calculate(self):
        print("Calculating...")

class Display:
    def display(self):
        print("Display")

class SmartPhone(Display, Computer):
    pass

iphone = SmartPhone()



Завдання 1: Створи клас "Тварина", який має властивості, спільні для всіх тварин, і потім
створи підкласи, наприклад, "Собака" та "Кіт", які успадковують властивості від "Тварини"

class Animal:
    legs = 4
    eyes = 2
    tail = 1

class Dog(Animal):
    name = "Rex"
    age = 3
    breed = "Labrador"
class Cat(Animal):
    name = "Murzik"
    age = 5
    color = "grey"

dog = Dog()
cat = Cat()

print("Dog description: ", "legs: ", dog.legs, ", eyes: ", dog.eyes, ", tails: ", dog.tail, ", name: ", dog.name, ", age: ", dog.age, ", breed: ", dog.breed)
print("Cat description: ", "legs: ", cat.legs, ", eyes: ", cat.eyes, ", tails: ", cat.tail, ", name: ", cat.name, ", age: ", cat.age, ", breed: ", cat.color)
'''
