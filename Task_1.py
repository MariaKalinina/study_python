from sys import argv
try:
    hours, fee, bonus = argv[1:]
    hours, fee, bonus = float(hours), float(fee), float(bonus)
    salary = hours * fee + bonus
    print(f"Salary of the employee in this month - {salary}")
except ValueError:
    print("You must add 3 numbers!")
