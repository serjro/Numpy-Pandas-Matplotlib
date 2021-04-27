class Selfroad:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class road(Selfroad):
    def __init__(self,length,width):
        super().__init__(length,width)
    def mass(self):
        print(f"Масса асфальта - {self.length*self.width*25*0.005} т.")

road_exe=road(5000,20)
road_exe.mass()