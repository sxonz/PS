testcase = int(input())
ans = []
for test in range(testcase):
    n,m = map(int,input().split())
    p = list(range(n+1))
    def F(x):
        if x-p[x]:p[x] = F(p[x])
        return p[x]
    def U(a,b):
        a,b = F(a),F(b)
        if a<b:
            p[b] = a
        else:
            p[a] = b
    edges = []
    for i in range(m):
        a,b,c = map(int,input().split())
        edges.append((-c,a,b))
    edges.sort()
    cost = -int(1e9)
    for c,a,b in edges:
        if F(a)-F(b):
            U(a,b)
            cost = max(cost,c)
            if F(1) == F(n):
                ans.append(-cost)
                break
for i in range(testcase):
    print(f"Scenario #{i+1}:")
    print(ans[i])
    print()
