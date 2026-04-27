n,m = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
ms = [i for i in d if i<0]
ps = [i for i in reversed(d) if i>0]
dis = []
while ms:
    c = 0
    for i in range(m):
        if not ms:
            break
        c = min(c,ms.pop(0))
    dis.append(-c)
while ps:
    c = 0
    for i in range(m):
        if not ps:
            break
        c = max(c,ps.pop(0))
    dis.append(c)
dis.sort()
ans = dis.pop()
print(sum([i*2 for i in dis])+ans)