""" Операции с комплексными числами"""


class ComplexNum:
    def __init__(self):
        self.a = input("Enter real number a of the complex: ")
        self.b = input("Enter real number b of the complex: ")
        try:
            self.num = complex(int(self.a), int(self.b))
        except TypeError as v:
            print(v)

    def __add__(self, other):
        try:
            # return self.num + other.num # более простая реализация
            add_a = int(self.a) + int(other.a)
            add_b = int(self.b) + int(other.b)
            add_complex = complex(add_a, add_b)
            return add_complex
        except AttributeError as ae:
            return ae

    def __mul__(self, other):
        try:
            return self.num * other.num
        except AttributeError as ae:
            return ae


n_1 = ComplexNum()
n_2 = ComplexNum()
print(f"Sum of complex numbers n_1 and n_2 is {n_1 + n_2}")
print(f"Multiplication of complex numbers n_1 and n_2 is {n_1 * n_2}")
