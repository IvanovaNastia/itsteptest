class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, my name is {self.name}. I am {self.age} years old"


den = Human("Denis", 30)
print(den)