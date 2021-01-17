# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
n = int(input("Задайте любое число n: "))
nn = int(f"{n}{n}")
nnn = int(f"{n}{n}{n}")
print("Сумма чисел n + nn + nnn: ")
print(n + nn + nnn)
