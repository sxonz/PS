d = {'666'}
for i in range(4):
    tmp = set()
    for j in d:
        for k in range(10):
            tmp.add(str(k)+j)
            tmp.add(j+str(k))
    for j in tmp:
        d.add(j)
d = list(sorted(set([int(i) for i in d])))
n = int(input())
print(d[n-1])