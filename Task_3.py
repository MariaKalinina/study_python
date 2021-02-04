class Worker:
    def __init__(self):
        self.name = input("Enter name: ")
        self.surname = input("Enter surname: ")
        self.position = input("Enter position: ")
        self._income = {"wage": input("Enter wage: "), "bonus": input("Enter bonus: ")}


class Position(Worker):
    def get_full_name(self):
        print(f"Full name of {self.position} is {self.name} {self.surname}")

    def get_total_income(self):
        try:
            total_income = int(self._income.get("wage")) + int(self._income.get("bonus"))
            print(f"Total income of {self.name} {self.surname} is {total_income}")
        except ValueError as k:
            print(k)


worker_1 = Position()
worker_1.get_full_name()
worker_1.get_total_income()
