class Car:

    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def set_speed(self, speed):
        self.__speed = speed + 5

    def set_break(self, speed):
        self.__speed = speed - 5
