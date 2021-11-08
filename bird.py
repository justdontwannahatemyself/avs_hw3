from animal import *
import random


class Bird(Animal):
    def __init__(self):
        self.name = ""
        self.weight = 0
        self.migration = False

    def from_file(self, arr):
        self.name = arr[0]
        self.weight = int(arr[1])
        if self.weight <= 0:
            raise ValueError("Вес не может быть отрицательным или равным нулю")
        a = int(arr[2])
        if a != 1:
            self.migration = False
        else:
            self.migration = True

    def random_parameters(self):
        length = random.randint(1, 10)
        for i in range(0, length):
            self.name += chr(random.randrange(97, 97 + 26))
        self.weight = random.randint(1, 1000000)
        a = random.randint(0, 1)
        if a != 1:
            self.migration = False
        else:
            self.migration = True

    def write(self, ostream):
        ostream.write(
            f"It is a Bird.Name is {self.name}, ability to migrate: {self.migration}, weight is {self.weight},"
            f" fraction is {Animal.fraction(self.name, self.weight)} "
        )
    def print(self):
        print(
            f"It is a Bird.Name is {self.name}, ability to migrate: {self.migration}, weight is {self.weight},"
            f" fraction is {Animal.fraction(self.name, self.weight)}"
        )
