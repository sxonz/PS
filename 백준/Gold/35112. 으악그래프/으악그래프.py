n,m = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(m)]

parents = list(range(n+1))
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]
def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b

cnt = 0
flag = True
for a,b in d:
    if find(a) == find(b):
        if flag:
            flag = False
        else:
            print("No")
            break
    else:
        union(a,b)
else:
    print("Yes")
