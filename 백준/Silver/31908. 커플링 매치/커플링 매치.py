n = int(input())
d = dict()
revd = dict()
couple = []
ring = []
for i in range(n):
    a,b = input().split()
    ring.append(b)
    if b == '-':
        continue
    else:
        if b in d:
            couple.append((d[b],a))
        else:
            d[b] = a
            revd[a] = b


res = []
l = 0
for i in couple:
    if ring.count(revd[i[0]]) < 3:
        res.append(i)
        l += 1
print(l)
for i in res:
    print(*i)
