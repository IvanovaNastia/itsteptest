#Завдання 4

class Device:
    def __init__(self, name):
        self.name = name
        self.on = False

    def turn_on(self):
        if not self.on:
            self.on = True
            print(f"{self.name} увімкнено.")
        else:
            print(f"{self.name} вже увімкнено.")

    def turn_off(self):
        if self.on:
            self.on = False
            print(f"{self.name} вимкнено.")
        else:
            print(f"{self.name} вже вимкнено.")

class Lamp(Device):
    def __init__(self, name):
        super().__init__(name)

class TV(Device):
    def __init__(self, name):
        super().__init__(name)


lamp = Lamp("Настільна лампа")
tv = TV("Samsung")

lamp.turn_on()
tv.turn_on()

lamp.turn_off()
tv.turn_off()