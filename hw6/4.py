class Car:
    def __init__(self, name,  color, speed, is_police):
        self.speed = speed
        self.color = name
        self.is_police = is_police
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self,direction):
        if direction==0:
            print("Машина повернула на лево")
        else:
            print("Машина повернула на право")
    def show_speed(self):
        print(f"Скорость - {self.speed}")

class TownCar(Car):
    def show_speed(self):
        print(f"Скорость - {self.speed}")
        if self.speed > 60: print("Превышение скорости!")
class SportCar(Car):
    print()

class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость - {self.speed}")
        if self.speed > 40: print("Превышение скорости!")
        else:print(f"Скорость - {self.speed}")
class PoliceCar(Car):
    print()

tcar=TownCar("TownHero","Yellow",100,0)
tcar.go()
tcar.show_speed()
tcar.turn(1)
tcar.stop()