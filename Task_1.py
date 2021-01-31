with open("text_1.txt.", "w", encoding="utf-8") as t_1:
    enter = input("Enter string to add it to the file:")
    while enter != "":
        to_file = t_1.writelines([str(enter), "\n"])
        enter = input("Enter string to add it to the file:")
