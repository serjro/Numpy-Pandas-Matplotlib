import json
firm=[]
profit=[]
mid=[]
firm_profit=dict()
with open('task 7.txt', 'r') as fp:
    for n, line in enumerate(fp, 1):
        line = line.rstrip('\n')
        firm.append(line.split()[0])
        profit.append(int(line.split()[2])-int(line.split()[3]))
for i in range(len(profit)):
    if profit[i]>0:mid.append(profit[i])
    firm_profit.update({firm[i]:profit[i]})
    #else:mid.append(0)
firm_profit.update({"average_profit":sum(mid)/len(mid)})
print(firm_profit)
print(f"Средняя прибыль - {sum(mid)/len(mid)}")

with open("my_file.json", "w") as write_f:
    json.dump(firm_profit, write_f)