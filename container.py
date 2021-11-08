from random import randint
from bird import Bird
from beast import Beast
from fish import Fish
from typing import List
import typing


class Container:
    def __init__(self):
        self.store = []

    def in_random(self, animal_num: int):
        for i in range(animal_num):
            animal_index = randint(1, 3)
            if animal_index == 1:
                animal = Fish()
                animal.random_parameters()
                self.store.append(animal)
            if animal_index == 2:
                animal = Beast()
                animal.random_parameters()
                self.store.append(animal)
            if animal_index == 3:
                animal = Bird()
                animal.random_parameters()
                self.store.append(animal)

    def read_file(self, filename: str):
        with open(filename, 'r') as file:
            animal_index = int(file.readline())
            while animal_index != 0:
                if animal_index == 1:
                    animal = Fish()
                    animal.from_file(file.readline().split())
                    self.store.append(animal)
                if animal_index == 2:
                    animal = Beast()
                    animal.from_file(file.readline().split())
                    self.store.append(animal)
                if animal_index == 3:
                    animal = Bird()
                    animal.from_file(file.readline().split())
                    self.store.append(animal)
                animal_index = int(file.readline())

    def write(self, ostream: typing.IO):
        ostream.write(f"Container is store {len(self.store)} animals:\n")
        for animal in self.store:
            animal.write(ostream)
            ostream.write("\n")

    def print(self):
        print("Container is store", len(self.store), "animals:")
        for animal in self.store:
            animal.print()

    def shell_sort(self):
        d = len(self.store) // 2
        while d != 0:
            for i in range(d, len(self.store), d):
                j = i
                while j > 0 and (self.store[j - d].fraction((self.store[j-d]).name, (self.store[j-d]).weight) >
                                 self.store[j].fraction((self.store[j]).name, (self.store[j]).weight)):
                    self.store[j - d], self.store[j] = self.store[j], self.store[j - d]
                    j -= d
            d //= 2
