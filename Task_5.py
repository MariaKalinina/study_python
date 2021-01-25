def sum_func():
    summary = 0
    while True:
        numbers_list = input("Enter list of numbers using space between them: ")
        numbers_list = numbers_list.split()
        for i in numbers_list:
            if i == "x":
                print(f"Final sum is {summary}")
            else:
                try:
                    summary += int(i)
                except ValueError:
                    print("Press x to exit")
        print(summary)


sum_func()
