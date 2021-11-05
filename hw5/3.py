surnames= []
salary=[]
min_salary=[]
min_surnames= []
mid=0
with open('task 3.txt', 'r') as fp:
    for n, line in enumerate(fp, 1):
        line = line.rstrip('\n')
        surnames.append(line.split()[0])
        salary.append(int(line.split()[2]))
        if int(line.split()[2])<20000:
            min_surnames.append(line.split()[0])
            min_salary.append(line.split()[2])

print(min_surnames)
print(min_salary)
print(f"Средняя зарплата - {sum(salary)/len(salary)}")
