class OnlyNumbers(Exception):
    def __init__(self, text):
        self.text = text


while True:
    num = input("Enter number to add it in the list or 's' if you want to exit: ")
    fin_list = []
    if num == "s" or num == "S":
        print(f"Final list is {fin_list}")
        break
    try:
        if not num.isdigit():
            raise OnlyNumbers("Only numbers can be added to the list")
    except OnlyNumbers as ON:
        print(ON)
    else:
        num = int(num)
        fin_list.append(num)
        print(fin_list)
