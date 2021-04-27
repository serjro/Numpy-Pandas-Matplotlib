class Cellular:
    def __init__(self,num):
        self.num=num

    def __add__(self, other):
        return self.num+other.num

    def __sub__(self, other):
        return self.num-other.num

    def __mul__(self, other):
        return self.num*other.num

    def __floordiv__(self, other):
        return self.num//other.num

    def make_order(self,rows):
        self.rows=rows
        return "\n".join(["*"*self.rows for _ in range(self.num//self.rows)])+"\n"+"*"*(self.num%self.rows)

cell1=Cellular(10)
cell2=Cellular(5)

print(cell1//cell2)
print(cell1.make_order(3))