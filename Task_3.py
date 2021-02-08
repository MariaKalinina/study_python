class Cell:
    def __init__(self, box_amount):
        self.box_amount = box_amount
        try:
            self.box_amount = int(self.box_amount)
        except ValueError:
            print("You must enter number in input!!!")

    def make_order(self, box_in_row):
        rows = self.box_amount // int(box_in_row)
        remaining = self.box_amount % int(box_in_row)
        one_row = "@" * box_in_row
        print_all_rows = f"{one_row}\n" * rows
        print_remaining = "@" * remaining
        return f"{print_all_rows}{print_remaining}"

    def __add__(self, other):
        add_cell = self.box_amount + other.box_amount
        return Cell(add_cell)

    def __sub__(self, other):
        sub_cell = self.box_amount - other.box_amount
        if sub_cell > 0:
            return Cell(sub_cell)
        else:
            return f"Amount of boxes is less then 0"

    def __mul__(self, other):
        mul_cell = self.box_amount * other.box_amount
        return Cell(mul_cell)

    def __truediv__(self, other):
        div_cell = self.box_amount // other.box_amount
        return Cell(div_cell)


cell1 = Cell(input("Amount of boxes in the cell:"))
cell2 = Cell(input("Amount of boxes in the cell:"))
print(f"cell1 + cell2 = {cell1+cell2}")
print(f"cell1 - cell2 = {cell1-cell2}")
print(f"cell1 * cell2 = {cell1*cell2}")
print(f"cell1 / cell2 = {cell1/cell2}")
print(cell1.make_order(4))
