new_s=list("")
s=input().split()
int_func= lambda string: string.title()
for i in range(len(s)):new_s.append(int_func(s[i]))
print(" ".join(new_s))