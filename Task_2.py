my_list = input("Enter list of items using space between them: ")
new_list = my_list.split()
print(f"Your list: {new_list}")
if len(new_list) % 2 == 0:
    new_list[::2], new_list[1::2] = new_list[1::2], new_list[::2]
    print(new_list)
else:
    last_el = new_list.__getitem__(-1)
    new_list.pop(-1)
    new_list[::2], new_list[1::2] = new_list[1::2], new_list[::2]
    new_list.append(last_el)
    print(f"Your list after converting: {new_list}")
