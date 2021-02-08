from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def fabric_cons(self):
        pass

    def __add__(self, other):
        total_cons = self.fabric_cons + other.fabric_cons
        return total_cons


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 36:
            self.__size = 36
        elif size > 60:
            self.__size = 60
        else:
            self.__size = size

    @property
    def fabric_cons(self):
        try:
            consumption = self.size / 6.5 + 0.5
            return consumption
        except ValueError:
            print("Size must be given as a number (float or integer)")


class Suite(Clothes):
    def __init__(self, height):
        self.height = height
        # self.color = input("Color of the suite:")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1.65:
            self.__height = 1.65
        elif height > 2.00:
            self.__height = 2.00
        else:
            self.__height = height

    @property
    def fabric_cons(self):
        try:
            consumption = (2 * self.height + 0.3)
            return consumption
        except ValueError:
            print("Size must be given as a number (float or integer)")


coat1 = Coat(68)
coat2 = Coat(48)
coat3 = Coat(32)
print(f"To sew the coat of {coat1.size} size we will need "
      f"{coat1.fabric_cons:.2f} m of fabric")
print(f"To sew the coat of {coat2.size} size we will need "
      f"{coat2.fabric_cons:.2f} m of fabric")
print(f"To sew the coat of {coat3.size} size we will need "
      f"{coat3.fabric_cons:.2f} m of fabric")
suite1 = Suite(1.55)
suite2 = Suite(1.85)
suite3 = Suite(2.5)
print(f"To sew the suite for {suite1.height} m height we will need "
      f"{suite1.fabric_cons:.2f} m of fabric")
print(f"To sew the suite for {suite2.height} m height we will need "
      f"{suite2.fabric_cons:.2f} m of fabric")
print(f"To sew the suite for {suite2.height} m height we will need "
      f"{suite2.fabric_cons:.2f} m of fabric")
print(f"Total consumption of fabric is {coat2 + suite2:.2f}")
# print(f"Color of Suite2 is {suite2.color}")
