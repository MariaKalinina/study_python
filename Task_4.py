def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x > 0 > y:
            power_x = x ** y
            print("Result: x to the power of y = ", power_x)
        else:
            print("x must be > 0 and y must be < 0!")
    except ValueError as k:
        print(k)


my_func(input("Enter number x > 0: "), input("Enter number y < 0: "))
