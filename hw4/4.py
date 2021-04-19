from random import randrange
my_list = [randrange(10) for el in range(10)]
print(f"Исходный список: {my_list}")
print(f"Решение: {list(el for el in my_list if my_list.count(el)==1)}")