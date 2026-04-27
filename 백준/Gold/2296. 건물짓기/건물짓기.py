n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()
incv = dict()
decv = dict()
for i in d:
    m = 0
    m2 = 0
    for j in incv:
        if j < i[1]:
            m = max(m,incv[j])
        else:
            m2 = max(m2,decv[j])
    incv[i[1]] = m+i[2]
    decv[i[1]] = m2+i[2]
print(max(max(incv.values()),max(decv.values())))