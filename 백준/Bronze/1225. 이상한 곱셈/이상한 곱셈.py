a,b = input().split()
res = 0
tmp = sum([int(i) for i in a])
for j in b:
    res += tmp*int(j)
print(res)