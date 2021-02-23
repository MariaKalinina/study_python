class Date:
    def __init__(self):
        self.date = str(input("Введите дату в формате чч-мм-гггг:"))

    @classmethod
    def mode(cls, obj):
        date = obj.date
        date_mode = []
        for i in date.split("-"):
            date_mode.append(i)
        try:
            return f"Day {int(date_mode[0])}, month - {int(date_mode[1])}, year - {int(date_mode[2])}"
        except ValueError as k:
            return k

    @staticmethod
    def validation(day, month, year):
        if 0 <= year <= 2021:
            if 1 <= month <= 12:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if 1 <= day <= 31:
                        return f"ok"
                    else:
                        return f"В январе, марте, мае, июле, августе, октябре и декабре 31 день"
                elif month in [4, 6, 9, 11]:
                    if 1 <= day <= 30:
                        return f"ok"
                    else:
                        return f"В апреле, июне, сентябре и носябре 30 дней"
                elif year % 4 != 0:
                    if month in [2]:
                        if 1 <= day <= 29:
                            return f"ok"
                        else:
                            return f"В феврале невисокосного года 28 дней"
                elif year % 4 == 0:
                    if month in [2]:
                        if 1 <= day <= 28:
                            return f"ok"
                        else:
                            return f"В феврале високосного года 29 дней"
            else:
                return f"В году всего 12 месяцев"
        else:
            return f"Принимаем год от 0 но 2021 н.э."

    def get_date(self):
        d = self.date.split("-")
        try:
            return int(d[0])
        except ValueError as k:
            return k

    def get_month(self):
        d = self.date.split("-")
        try:
            return int(d[1])
        except ValueError as k:
            return k

    def get_year(self):
        d = self.date.split("-")
        try:
            return int(d[2])
        except ValueError as k:
            return k


a = Date()
print(Date.mode(a))
print(a.validation(a.get_date(), a.get_month(), a.get_year()))
