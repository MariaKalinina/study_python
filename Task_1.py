def my_first_func(div_1, div_2):

    try:
        div_1 = int(div_1)
        div_2 = int(div_2)
        division = int(div_1) / int(div_2)
        print(f"{division:.2f}")
    except ValueError:
        print("You entered wrong symbols, you must enter numbers!")
    except ZeroDivisionError as t:
        print(t)


my_first_func(input("Enter number: "), input("Enter divisor(!=0): "))
