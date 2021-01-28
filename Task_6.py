from itertools import count, cycle

list_1 = []
for el in count(3):
    list_1.append(el)
    if el >= 10:
        print(list_1)
        c = 0
        for n in cycle(list_1):
            if c > 20:
                break
            print(n)
            c += 1
        quit()
