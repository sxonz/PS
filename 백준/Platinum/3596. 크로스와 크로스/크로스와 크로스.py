n = int(input())
g = [0,1,1,1,2,2]
for i in range(6,n+1):
    tmp = set()
    for j in range(3,6):
        tmp.add(g[i-j])
    for j in range(i-5+1):
        tmp.add(g[j]^g[i-j-5])
    for k in range(3000):
        if k not in tmp:
            g.append(k)
            break
print((bool(g[n])^1)+1)