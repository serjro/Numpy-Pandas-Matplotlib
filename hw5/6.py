sheets=dict()
razd=[":","(л)","(пр)","(лаб)"]
with open('task 6.txt', 'r') as fp:
    for n, line in enumerate(fp, 1):
        line = line.rstrip('\n')
        all=0
        for i in range(3):
            if line.split()[i+1].split(razd[i])[0]!='—':all=all+int(line.split()[i+1].split(razd[i+1])[0])
        sheets.update({line.split()[0].split(razd[0])[0]:all})
print(sheets)