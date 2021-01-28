from math import factorial
from itertools import count


def fact():
    for el in count(1):
        yield factorial(el)


generate = fact()
n = input("enter number to get its factorial: ")
c = 0
try:
    for i in generate:
        if c >= int(n):
            break
        else:
            c += 1
            print(f"Factorial {c} = {i}")
except ValueError as c:
    print(c)
