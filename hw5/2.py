with open('task 2.txt', 'r') as fp:
     for n, line in enumerate(fp, 1):
         line = line.rstrip('\n')
         print(f"количества слов в {n} строке:  - {line.count(' ')+1}")
         b=n
print(f"\nколичество строк - {n}")