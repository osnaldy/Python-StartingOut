class Pet:

    def __init__(self, name, animal, age):
        self.__name = name
        self.__animal_type = animal
        self. __age = age

    def set_name(self,name):
        self.__name = name

    def set_animal_type(self,animal):
        self.__animal_type = animal

    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


