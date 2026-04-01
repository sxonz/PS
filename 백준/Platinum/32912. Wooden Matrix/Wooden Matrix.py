n = int(input())
d = []
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        d.append((tmp[j],i,j))

d.sort()
p = list(range(n))
node = [[i] for i in range(n)]
distance = [[0]*n for i in range(n)]
def F(x):
    if x!=p[x]:
        p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        p[b] = a
        node[a] += node[b]
        node[b] = []
    else:
        p[a] = b
        node[b] += node[a]
        node[a] = []

flag = False
for c,a,b in d:
    if F(a) == F(b):
        if distance[a][b] != c:
            flag = True
            break
    else:
        for i in node[F(a)]:
            for j in node[F(b)]:
                distance[i][j] = distance[i][a] + c + distance[b][j]
                distance[j][i] = distance[i][a] + c + distance[b][j]
        U(a,b)
print("YNeos"[flag::2])
