class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def accelerateSpeed(self,speed):
        self.__speed = speed + 5

    def breakSpeed(self,speed):
        self.__speed = speed - 5

    def get_speed(self):
        return self.__speed