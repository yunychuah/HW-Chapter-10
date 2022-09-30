import random 

class Insect:
    def __init__(self):
        self.__wings = 2
        self.__legs = 4
        self.__flight = 0


    def flight_length(self):
        self.__flight = random.randint(1,10)

    def get_flight(self):
        return self.__flight
