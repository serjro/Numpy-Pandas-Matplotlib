from random import randrange
my_list = [randrange(10) for el in range(10)]
print(f"Исходный список: {my_list}")
print(f"Решение: {list(my_list[el] for el in range(1,len(my_list)) if my_list[el-1] < my_list[el])}")