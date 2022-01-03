
sum=0
b=1
def stroka():
    global sum,b
    s=input("Введите строку чисел - ").split()
    for i in range(len(s)):
        if s[i]!="@" and b!=0:sum=sum+int(s[i])
        else:b=0
    print(sum)
    return b
while b!=0:b=stroka()