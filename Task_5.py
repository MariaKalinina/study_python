from functools import reduce

thousand = [n for n in range(100, 1001, 2)]
print(thousand)
print(reduce(lambda n, m: n*m, thousand))
