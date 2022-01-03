def my_func(x, y):
    if x>0 and y<0 and -y==int(abs(y)):
        for i in range(int(abs(y))-1): x=x*x
        return 1/x
    else:print("Введены некорректные значения")
print(my_func(2, -2))