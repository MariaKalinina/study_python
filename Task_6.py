enter = ""
goods = []
analytics = {"name": [], "price": [], "amount": [], "units": []}
i = 0
while enter == "":
    i += 1
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    amount = input("Enter amount: ")
    unit = input("Enter units of calculation:")
    item = (i, {"name": name, "price": price, "amount": amount, "units": unit})
    goods.append(item)
    print(goods)
    enter = input("Press Enter to continue or any other button+Enter to exit:").upper()
while True:
    print("Do you want to see analytics? ")
    choice = input("Press 1, if yes, press 0, if not (exit): ")
    if choice == 0:
        break
    for item in goods:
        analytics["name"].append(item[1]["name"])
        analytics["price"].append(item[1]["price"])
        analytics["amount"].append(item[1]["amount"])
        analytics["units"].append(item[1]["units"])
    print(analytics)
