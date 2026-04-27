ans = []
while True:
    r = input()
    if r == '0':
        break
        sus
    n,m = map(int,r.split())
    edges = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges.append((c,a,b))
    edges.sort()
    p = list(range(n+1))
    def f(x):
        if x-p[x]:p[x]=f(p[x])
        return p[x]
    cost = 0
    for c,a,b in edges:
        a,b = f(a),f(b)
        if a-b:
            p[a] = p[b] = min(a,b)
            cost += c
    ans.append(cost)
    input()
for i in ans:
    print(i)