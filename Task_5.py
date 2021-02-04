class Stationery:
    def __init__(self):
        self.title = input("Type title of stationery item: ")

    def draw(self):
        return f"Запуск отрисовки c помощью {self.title}."


class Pen(Stationery):
    pen_type = "ball pen"

    def draw(self):
        return f"This pen {self.title} draws smooth lines"


class Pencil(Stationery):
    def draw(self):
        return f"This pencil {self.title} is perfect for hatching"


class Handle(Stationery):
    def draw(self):
        return f"{self.title} is highlighting important points in the text"


Parker = Pen()
print(Parker.draw())
print(Parker.pen_type)
Silverhof = Pencil()
print(Silverhof.draw)
LightMark = Handle()
print(LightMark.draw)
