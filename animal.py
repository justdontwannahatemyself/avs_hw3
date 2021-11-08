import typing


class Animal:
    def print(self):
        pass

    def write(self, ostream: typing.IO):
        pass

    def from_file(self, int_array: typing.List[int]):
        pass

    def random_parameters(self):
        pass
        
    @staticmethod
    def fraction(name, weight):
        cnt = 0
        for i in range(0, len(name)):
            cnt += ord(name[i])
        return cnt / float(weight)
