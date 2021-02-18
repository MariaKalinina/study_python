class MyZeroDiv(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        dividend = float(input("Enter number which you want to divide: "))
        divisor = float(input("Enter divisor: "))
        if divisor == 0:
            raise MyZeroDiv("We can't divide by 0!")
    except MyZeroDiv as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print(dividend / divisor)
        break

