from functools import reduce
def my_func(prev_el, el):
    return prev_el * el
def generator():
    for el in range(1,n+1):
        yield el
n=5
g = generator()
my_list=[el for el in g]
print(reduce(my_func, my_list))