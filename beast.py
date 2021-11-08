from animal import *
import random


class Beast(Animal):
    def __init__(self):
        self.name = ""
        self.weight = 0
        self.meal = 0

    def from_file(self, arr):
        self.name = arr[0]
        self.weight = int(arr[1])
        if self.weight <= 0:
            raise ValueError("Вес не может быть отрицательным или равным нулю")
        self.meal = int(arr[2])

    def random_parameters(self):
        length = random.randint(1, 10)
        for i in range(0, length):
            self.name += chr(random.randrange(97, 97 + 26))
        self.weight = random.randint(1, 1000000)
        self.meal = random.randint(1, 3)

    def write(self, ostream):
        ostream.write(
            f"It is Beast.Name is {self.name}, type is {self.beasts_meal()}, weight is {self.weight},"
            f" fraction is {Animal.fraction(self.name, self.weight)} "
        )
    def print(self):
        print(
            f"It is Beast.Name is {self.name}, type is {self.beasts_meal()}, weight is {self.weight},"
            f" fraction is {Animal.fraction(self.name, self.weight)} "
        )

    def beasts_meal(self):
        if self.meal == 1:
            return "predator"
        if self.meal == 2:
            return "herbivores"
        if self.meal == 3:
            return "insectivores"
        return "none"
