def max_two(s_1, s_2, s_3):
    try:
        s_list = [int(s_1), int(s_2), int(s_3)]
        s_list.remove(min(s_list))
        max_1 = s_list[0]
        max_2 = s_list[1]
        summary = max_1 + max_2
        print(f"Summ of 2 biggest numbers of your list:", summary)
    except ValueError:
        print("You entered wrong symbols, you must enter numbers!")


max_two(input("Enter number:"), input("Enter number:"), input("Enter number:"))
