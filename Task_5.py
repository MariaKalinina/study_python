from random import randint

t_5 = open("text_5.txt.", "r+", encoding="utf-8")
rand_list = []
c = 0
try:
    for i in range(0, 100):
        if c >= 5:
            break
        else:
            c += 1
            i = randint(0, 100)
            rand_list.append(i)
    rand_str = ', '.join(str(e) for e in rand_list)
    to_file = t_5.writelines(f"{rand_str}\n")
    for lines in t_5:
        content = t_5.readline()
        content = content.split(", ")
        print(f"The list of numbers in the line: {content}")
        for i in content:
            sum_all = sum(map(int, content))
        print(f"Sum of numbers in the list above: {sum_all}")
except ValueError as c:
    print(c)
t_5.close()
