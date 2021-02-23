class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    @property
    def dict(self):
        return self._dict


class OfficeEquipment:
    def __init__(self, name, colored):
        self.name = name
        self.colored = colored
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'


class Printer(OfficeEquipment):
    def __init__(self, name, colored, model, print_t):
        super().__init__(name, colored)
        self.model = model
        self.print_t = print_t

    def __repr__(self):
        return f"{self.name} {self.model} {self.colored} {self.print_t}"

    def printing(self):
        return f"{self.name} {self.model} prints documents for you"


class Scanner(OfficeEquipment):
    def __init__(self, name, colored, model, res):
        super().__init__(name, colored)
        self.model = model
        self.res = res

    def __repr__(self):
        return f"{self.name} {self.model} {self.colored} {self.res}"

    def scan(self):
        return f"{self.name} {self.model} scans your passport"


class Copier(OfficeEquipment):
    def __init__(self, name, colored, model, res):
        super().__init__(name, colored)
        self.model = model
        self.res = res

    def __repr__(self):
        return f"{self.name} {self.model} {self.colored} {self.res}"

    def copy(self):
        return f"{self.name} {self.model} copies 100 pages"


warehouse1 = Warehouse()
while True:
    add_option = int(input("Which office equipment do you want to add to the warehouse1? \n"
                           "1 - Printer\n"
                           "2 - Scanner\n"
                           "3 - Copier\n"
                           "0 - exit"))
    if add_option == 1:
        choose_brand = int(input("Item of which brand do you want to add to the warehouse1?\n"
                                 "1 - HP\n"
                                 "2 - LBP\n"
                                 "0 - exit"))
        if choose_brand == 1:
            choose_type = int(input("Which type of office equipment do you want to add to the warehouse1? \n"
                                    "1 - black&white\n"
                                    "2 - colored\n"
                                    "0 - exit"))
            if choose_type == 1:
                laser_jet = int(input("Which type of printer do you want to add to the warehouse1? \n"
                                      "1 - laser\n"
                                      "2 - jet\n"
                                      "0 - exit"))
                if laser_jet == 1:
                    model_number = input("Enter model number")
                    HP_bw_las = Printer("HP", "black&white", model_number, "laser")
                    warehouse1.add_to(HP_bw_las)
                if laser_jet == 2:
                    model_number = input("Enter model number")
                    HP_bw_jet = Printer("HP", "black&white", model_number, "jet")
                    warehouse1.add_to(HP_bw_jet)
            if choose_type == 2:
                laser_jet = int(input("Which type of printer do you want to add to the warehouse1? \n"
                                      "1 - laser\n"
                                      "2 - jet\n"
                                      "0 - exit"))
                if laser_jet == 1:
                    model_number = input("Enter model number")
                    HP_col_las = Printer("HP", "colored", model_number, "laser")
                    warehouse1.add_to(HP_col_las)
                if laser_jet == 2:
                    model_number = input("Enter model number")
                    HP_col_jet = Printer("HP", "colored", model_number, "jet")
                    warehouse1.add_to(HP_col_jet)
                if laser_jet == 0:
                    break
            if choose_type == 0:
                break
        if choose_brand == 2:
            choose_type = int(input("Which type of office equipment do you want to add to the warehouse1? \n"
                                    "1 - black&white\n"
                                    "2 - colored\n"
                                    "0 - exit"))
            if choose_type == 1:
                laser_jet = int(input("Which type of printer do you want to add to the warehouse1? \n"
                                      "1 - laser\n"
                                      "2 - jet\n"
                                      "0 - exit"))
                if laser_jet == 1:
                    model_number = input("Enter model number")
                    LBP_bw_las = Printer("HP", "black&white", model_number, "laser")
                    warehouse1.add_to(LBP_bw_las)
                if laser_jet == 2:
                    model_number = input("Enter model number")
                    LBP_bw_jet = Printer("HP", "black&white", model_number, "jet")
                    warehouse1.add_to(LBP_bw_jet)
            if choose_type == 2:
                laser_jet = int(input("Which type of printer do you want to add to the warehouse1? \n"
                                      "1 - laser\n"
                                      "2 - jet\n"
                                      "0 - exit"))
                if laser_jet == 1:
                    model_number = input("Enter model number")
                    LBP_col_las = Printer("HP", "colored", model_number, "laser")
                    warehouse1.add_to(LBP_col_las)
                if laser_jet == 2:
                    model_number = input("Enter model number")
                    LBP_col_jet = Printer("HP", "colored", model_number, "jet")
                    warehouse1.add_to(LBP_col_jet)
                if laser_jet == 0:
                    break
            if choose_type == 0:
                break
        if choose_brand == 0:
            break
    if add_option == 2:
        choose_brand = int(input("Item of which brand do you want to add to the warehouse1?\n"
                                 "1 - HP\n"
                                 "2 - LBP\n"
                                 "0 - exit"))
        if choose_brand == 1:
            choose_type = int(input("Which type of office equipment do you want to add to the warehouse1? \n"
                                    "1 - black&white\n"
                                    "2 - colored\n"
                                    "0 - exit"))
            if choose_type == 1:
                resolution = int(input("What is resolution of the adding scanner? \n"
                                       "1 - 300px\n"
                                       "2 - 600px\n"
                                       "0 - exit"))
                if resolution == 1:
                    model_number = input("Enter model number")
                    HP_bw_sc_300 = Scanner("HP", "black&white", model_number, "res = 300px")
                    warehouse1.add_to(HP_bw_sc_300)
                if resolution == 2:
                    model_number = input("Enter model number")
                    HP_bw_sc_600 = Scanner("HP", "black&white", model_number, "res = 600px")
                    warehouse1.add_to(HP_bw_sc_600)
            if choose_type == 2:
                resolution = int(input("What is resolution of the adding scanner? \n"
                                       "1 - 300px\n"
                                       "2 - 600px\n"
                                       "0 - exit"))
                if resolution == 1:
                    model_number = input("Enter model number")
                    HP_col_sc_300 = Scanner("HP", "black&white", model_number, "res = 300px")
                    warehouse1.add_to(HP_col_sc_300)
                if resolution == 2:
                    model_number = input("Enter model number")
                    HP_col_sc_600 = Scanner("HP", "black&white", model_number, "res = 600px")
                    warehouse1.add_to(HP_col_sc_600)
                if resolution == 0:
                    break
            if choose_type == 0:
                break
        if choose_brand == 2:
            choose_type = int(input("Which type of office equipment do you want to add to the warehouse1? \n"
                                    "1 - black&white\n"
                                    "2 - colored\n"
                                    "0 - exit"))
            if choose_type == 1:
                resolution = int(input("What is resolution of the adding scanner? \n"
                                       "1 - 300px\n"
                                       "2 - 600px\n"
                                       "0 - exit"))
                if resolution == 1:
                    model_number = input("Enter model number")
                    LBP_bw_sc_300 = Scanner("HP", "black&white", model_number, "res = 300px")
                    warehouse1.add_to(LBP_bw_sc_300)
                if resolution == 2:
                    model_number = input("Enter model number")
                    LBP_bw_sc_600 = Scanner("HP", "black&white", model_number, "res = 600px")
                    warehouse1.add_to(LBP_bw_sc_600)
            if choose_type == 2:
                resolution = int(input("What is resolution of the adding scanner? \n"
                                       "1 - 300px\n"
                                       "2 - 600px\n"
                                       "0 - exit"))
                if resolution == 1:
                    model_number = input("Enter model number")
                    LBP_col_sc_300 = Scanner("HP", "black&white", model_number, "res = 300px")
                    warehouse1.add_to(LBP_col_sc_300)
                if resolution == 2:
                    model_number = input("Enter model number")
                    LBP_col_sc_600 = Scanner("HP", "black&white", model_number, "res = 600px")
                    warehouse1.add_to(LBP_col_sc_600)
                if resolution == 0:
                    break
            if choose_type == 0:
                break
        if choose_brand == 0:
            break
    if add_option == 3:
        choose_brand = int(input("Item of which brand do you want to add to the warehouse1?\n"
                                 "1 - HP\n"
                                 "2 - LBP\n"
                                 "0 - exit"))
        if choose_brand == 1:
            choose_type = int(input("Which type of office equipment do you want to add to the warehouse1? \n"
                                    "1 - black&white\n"
                                    "2 - colored\n"
                                    "0 - exit"))
            if choose_type == 1:
                resolution = int(input("What is resolution of the adding copier? \n"
                                       "1 - 300px\n"
                                       "2 - 600px\n"
                                       "0 - exit"))
                if resolution == 1:
                    model_number = input("Enter model number")
                    HP_bw_cop_300 = Copier("HP", "black&white", model_number, "res = 300px")
                    warehouse1.add_to(HP_bw_cop_300)
                if resolution == 2:
                    model_number = input("Enter model number")
                    HP_bw_cop_600 = Copier("HP", "black&white", model_number, "res = 600px")
                    warehouse1.add_to(HP_bw_cop_600)
            if choose_type == 2:
                resolution = int(input("What is resolution of the adding scanner? \n"
                                       "1 - 300px\n"
                                       "2 - 600px\n"
                                       "0 - exit"))
                if resolution == 1:
                    model_number = input("Enter model number")
                    HP_col_cop_300 = Copier("HP", "black&white", model_number, "res = 300px")
                    warehouse1.add_to(HP_col_cop_300)
                if resolution == 2:
                    model_number = input("Enter model number")
                    HP_col_cop_600 = Copier("HP", "black&white", model_number, "res = 600px")
                    warehouse1.add_to(HP_col_cop_600)
                if resolution == 0:
                    break
            if choose_type == 0:
                break
        if choose_brand == 2:
            choose_type = int(input("Which type of office equipment do you want to add to the warehouse1? \n"
                                    "1 - black&white\n"
                                    "2 - colored\n"
                                    "0 - exit"))
            if choose_type == 1:
                resolution = int(input("What is resolution of the adding scanner? \n"
                                       "1 - 300px\n"
                                       "2 - 600px\n"
                                       "0 - exit"))
                if resolution == 1:
                    model_number = input("Enter model number")
                    LBP_bw_sc_300 = Copier("HP", "black&white", model_number, "res = 300px")
                    warehouse1.add_to(LBP_bw_sc_300)
                if resolution == 2:
                    model_number = input("Enter model number")
                    LBP_bw_sc_600 = Copier("HP", "black&white", model_number, "res = 600px")
                    warehouse1.add_to(LBP_bw_sc_600)
            if choose_type == 2:
                resolution = int(input("What is resolution of the adding scanner? \n"
                                       "1 - 300px\n"
                                       "2 - 600px\n"
                                       "0 - exit"))
                if resolution == 1:
                    model_number = input("Enter model number")
                    LBP_col_sc_300 = Copier("HP", "black&white", model_number, "res = 300px")
                    warehouse1.add_to(LBP_col_sc_300)
                if resolution == 2:
                    model_number = input("Enter model number")
                    LBP_col_sc_600 = Copier("HP", "black&white", model_number, "res = 600px")
                    warehouse1.add_to(LBP_col_sc_600)
                if resolution == 0:
                    break
            if choose_type == 0:
                break
        if choose_brand == 0:
            break
    if add_option == 0:
        break
print(warehouse1.dict)
warehouse1.extract('Printer')
print(warehouse1.dict)
