eng=["One","Two","Three","Four",""]
rus=["Один","Два","Три","Четыре",""]
inf = open("task 4_out.txt", "w")
with open('task 4.txt', 'r') as fp:
    for n, line in enumerate(fp, 1):
        line = line.rstrip('\n')
        if line.split()[0] == eng[n-1]: inf.write(rus[n-1] + ' — ' + line.split()[2] + "\n")
inf.close()
