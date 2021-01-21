# using list for season and dict for month's name
winter = (1, 2, 12)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)
valid_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
month_digit = int(input("Enter number of desired month (from 1 to 12): "))
while month_digit not in valid_numbers:
    month_digit = int(input("Enter number of desired month (from 1 to 12): "))
if month_digit in winter:
    print("Winter")
elif month_digit in spring:
    print("Spring")
elif month_digit in summer:
    print("Summer")
elif month_digit in autumn:
    print("Autumn")
month_names = {1: "January", 2: "February", 3: "March", 4: "April",
               5: "May", 6: "June", 7: "July", 8: "August",
               9: "September", 10: "October", 11: "November", 12: "December"}
if month_digit in month_names:
    print(month_names.get(month_digit))
