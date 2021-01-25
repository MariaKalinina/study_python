def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        y_abs = abs(y)
        x_pow = x
        if x > 0 > y:
            if y == -1:
                x = 1 / x
                print("Result: x to the power of y = ", x)
            elif y_abs > 1:
                for i in range(2, y_abs + 1):
                    x_pow = x_pow * x
                    y_abs -= 1
                x_pow = 1 / x_pow
                print("Result: x to the power of y = ", x_pow)
        else:
            print("x must be > 0 and y must be < 0!")
    except ValueError as k:
        print(k)


my_func(input("Enter number x > 0: "), input("Enter number y < 0: "))
