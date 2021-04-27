out_f = open("task 5.txt", "w")
out_f.write("1 2 3 4 5 6 7 8")
out_f.close()
b=[]
with open('task 5.txt', 'r') as fp:
        line = fp.readline()
        print(line)
        for n in line.split(): b.append(int(n))
        print(f"Сумма всех элементов - {sum(b)}")