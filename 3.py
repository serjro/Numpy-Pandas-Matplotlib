def my_func(arg_1, arg_2, arg_3):
    if arg_3 > arg_1 < arg_2: return arg_2 + arg_3
    if arg_1 > arg_2 < arg_3: return arg_1 + arg_3
    if arg_1 > arg_3 < arg_2: return arg_2 + arg_1
print(my_func(1, 2, 3))
