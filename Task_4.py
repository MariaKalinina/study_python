class Car:
    is_police = False

    def __init__(self):
        self.speed = input("Speed of the car is ")
        self.color = input("Color is")
        self.name = input("My name is")

    def go(self):
        print(f"Car {self.name} started movement.")

    def stop(self):
        print(f"Car {self.name} stopped.")

    def turn(self, direction):
        print(f"Car {self.name} turned {direction}.")

    def show_speed(self):
        print(f"Car {self.name} has speed {self.speed}.")


class TownCar(Car):
    def show_speed(self):
        try:
            self.speed = int(self.speed)
            if self.speed < 60:
                print(f"Car {self.name} has speed {self.speed}.")
            else:
                print(f"Car {self.name} has exceeded speed limit of 60 km/h!!!"
                      f"Your speed is {self.speed}. Reduce speed!")
        except ValueError as k:
            print(k)


class SportCar(Car):
    def drift(self):
        print(f"Car {self.name} is drifting \nWrooom!!!")


class WorkCar(Car):
    def show_speed(self):
        try:
            self.speed = int(self.speed)
            if self.speed < 40:
                print(f"Car {self.name} has speed {self.speed}.")
            else:
                print(f"Car {self.name} has exceeded speed limit of 40 km/h!!!"
                      f"Your speed is {self.speed}. Reduce speed!")
        except ValueError as k:
            print(k)


class PoliceCar(Car):
    is_police = True

    def chase(self):
        print(f"Police car {self.name} is chasing {SportCar}")


rider = SportCar()
kia = WorkCar()
robocar_Poli = PoliceCar()
skoda = TownCar()
rider.drift()
rider.show_speed()
robocar_Poli.chase()
print(robocar_Poli.is_police)
skoda.show_speed()
print(skoda.color)
kia.go()
kia.turn("left")
kia.show_speed()
kia.stop()
