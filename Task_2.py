class Road:
    def __init__(self):
        self._length = input("Enter length of the road: ")
        self._width = input("Enter width of the road: ")

    def mass_count(self):
        try:
            mass = int(self._length) * int(self._width) * 25 * 5
            return f"Mass of the road is {mass}"
        except ValueError as k:
            print(k)


road_1 = Road()
print(road_1.mass_count())
