'''
Завдання 1 Попрацюйте над складним класом, що породжений кількома класами.  У кожного з класів, від яких
успадковується результівний, мають бути ексклюзивні атрибути та методи, які доступні в дочірньому.



class Season:
    def __init__(self, name):
        self.name = name
    def get_season_name(self):
        return f"Це {self.name}"

class Temp:
    def temp(self, temp):
        self.temp = temp

    def describe_temp(self):
        return f"Температура зараз {self.temp} градусів Цельсія"


class Wind:
    def  wind(self, speed, direction):
        self.speed = speed
        self.direction = direction

    def describe_wind(self):
        return f"Вітер зараз {self.direction}, {self.speed} м/с"

class Weather(Season, Temp, Wind):
    def __init__(self, season_name, temp, wind_speed, direction, precipitation):
        Season.__init__(self, season_name)
        Temp.__init__(self, temp)
        Wind.__init__(self, wind_speed)
        Wind.__init__(self, direction)
        self.precipitation = precipitation

    def describe_weather(self):
        season_info = self.get_season_name()
        temp_info = self.describe_temp()
        wind_info = self.describe_wind()
        return f"{season_info}. {temp_info}. {wind_info}. Періодичні опади: {self.precipitation}"


today = Weather("Літо", 30, 2, "Північний", "Немає")

print(today.describe_weather())

'''

class Season:
    def __init__(self, name):
        self.name = name

    def get_season_name(self):
        return f"Це {self.name}"

class Temp:
    def __init__(self, temperature):
        self.temperature = temperature

    def describe_temperature(self):
        return f"Температура зараз {self.temperature} градусів Цельсія"

class Wind:
    def __init__(self, speed):
        self.speed = speed

    def describe_wind(self):
        return f"Вітер зараз {self.speed} м/с"

class Weather(Season, Temp, Wind):
    def __init__(self, season_name, temperature, wind_speed, precipitation):
        Season.__init__(self, season_name)
        Temp.__init__(self, temperature)
        Wind.__init__(self, wind_speed)
        self.precipitation = precipitation

    def describe_weather(self):
        season_info = self.get_season_name()
        temperature_info = self.describe_temperature()
        wind_info = self.describe_wind()
        return f"{season_info}. {temperature_info}. {wind_info}. Періодичні опади: {self.precipitation}"

today = Weather("Весна", 15, 3, "Немає")
print(today.describe_weather())
