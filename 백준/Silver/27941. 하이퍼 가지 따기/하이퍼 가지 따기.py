r = [dict() for i in range(11)]
for i in range(2047):
    tmp = list(map(int,input().split()))
    for j in range(11):
        if tmp[j] not in r[j]:
            r[j][tmp[j]] = 0
        r[j][tmp[j]] += 1

for i in r:
    print(min(i,key=lambda x:i[x]),end=' ')
