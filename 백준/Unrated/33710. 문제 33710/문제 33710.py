n,k = map(int,input().split())
d = input()
r = []
for i in range(n):
    for j in range(i+1,n):
        if d[i] == d[j] and d[i] != 'X':
            r.append(d[:i]+d[j+1:])
if r:
    m = min([len(i) for i in r])
else:
    m = len(d)
for i in r:
    if not i:
        print(0)
        break
    for j in range(len(i)):
        for k in range(j+1,len(i)):
            if i[j] == i[k] and i[j] != 'X':
                m = min(m,len(i)-(k-j+1))
else:
    print(m)