a=[1,2,3,4]
b=[4,3,2,1]
class Matrix:
    def __init__(self,list):
        self.list=list

    def __str__(self):
        return " ".join(map(str,[self.list[i]
                                 for i in range(int((len(self.list)+1)/2))]))+"\n"+\
               " ".join(map(str,[self.list[i] for i in
                                 range(int((len(self.list)+1)/2),int(len(self.list)))]))
    def __add__(self, other):
        a=[]
        for i in range(int((len(self.list)+1)/2)):
            for j in range(int((len(self.list)+1)/2)):
                a.append(self.list[i+j]+other.list[i+j])
        return " ".join(map(str,[a[i] for i in range(int((len(a)+1)/2))]))+\
               "\n"+" ".join(map(str,[a[i] for i in range(int((len(a)+1)/2),int(len(a)))]))

matrix1=Matrix(a)
matrix2=Matrix(b)

print(f"Матрица - 1:\n{matrix1} \n")
print(f"Матрица - 2:\n{matrix2} \n")
print(f"Сумма матриц:\n{matrix1+matrix2} \n")
