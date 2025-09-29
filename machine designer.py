class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def starting_the_car(self):
        return f'Автомобиль заведен'


    def car_shutdown(self):
        return f'Автомобиль заглушен'

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color







