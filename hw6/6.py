class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка карандашом.")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка ручкой.")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером.")


cpen = Pen("Рисунок")
cpen.draw()
cpencil = Pencil("Рисунок")
cpencil.draw()
cHandle = Handle("Рисунок")
cHandle.draw()