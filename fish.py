from animal import *
import random


class Fish(Animal):
    def __init__(self):
        self.name = ""
        self.weight = 0
        self.area = 0

    def from_file(self, arr):
        self.name = arr[0]
        self.weight = int(arr[1])
        if self.weight <= 0:
            raise ValueError("Вес не может быть отрицательным или равным нулю")
        self.area = int(arr[2])

    def random_parameters(self):
        length = random.randint(1, 10)
        for i in range(0, length):
            self.name += chr(random.randrange(97, 97 + 26))
        self.weight = random.randint(1, 1000000)
        self.area = random.randint(1, 3)

    def print(self):
        print(
            f"It is a Fish.Name is {self.name}, area is {self.fish_area()}, weight is {self.weight},"
            f" fraction is {Animal.fraction(self.name, self.weight)} "
        )

    def write(self, ostream):
        ostream.write(
            f"It is a Fish.Name is {self.name}, area is {self.fish_area()}, weight is {self.weight},"
            f" fraction is {Animal.fraction(self.name, self.weight)} "
        )

    def fish_area(self):
        if self.area == 1:
            return "lake"
        if self.area == 2:
            return "sea"
        if self.area == 3:
            return "river"
        return "none"
