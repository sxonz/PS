ans = []
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    edges = []
    p = dict()
    for i in range(m):
        a,b,cost = input().split()
        edges.append((int(cost),a,b))
        if a not in p:
            p[a] = a
        if b not in p:
            p[b] = b

    def F(x):
        if x != p[x]:p[x] = F(p[x])
        return p[x]
    
    def U(a,b):
        a,b = F(a),F(b)
        p[b] = a

    edges.sort(reverse=True)
    s,e = input().split()
    cost = int(1e6)
    for c,a,b in edges:
        if F(a) != F(b):
            U(a,b)
            cost = min(cost,c)
            if F(s) == F(e):
                break
    ans.append(cost)
for i in range(len(ans)):
    print(f'Scenario #{i+1}')
    print(f'{ans[i]} tons\n')