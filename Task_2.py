def personal_info(**kwargs):
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    year = input("Enter year of your birth: ")
    place = input("Enter name of the place where you live: ")
    email_id = input("Enter your email ID: ")
    phone = input("Enter your phone number: ")
    print("User's personal info. Name: ", name, ". Surname: ",surname,". Year of birth: ",
          year, ". Place of living: ", place, ". Email ID: ", email_id, "Phone number: ", phone)


personal_info()
