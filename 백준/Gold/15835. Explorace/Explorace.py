testcase = int(input())
ans = []
for _ in range(testcase):
    n,m = map(int,input().split())
    edges = []
    for i in range(m):
        a,b,c = map(int,input().split())
        edges += [(c,a,b)]
    edges.sort()

    p = list(range(n+1))
    def f(x):
        if x-p[x]: p[x] = f(p[x])
        return p[x]
    def u(a,b):
        a,b = f(a),f(b)
        if a<b:p[b] = a
        else:p[a] = b
    cost = 0
    for c,a,b in edges:
        if f(a)-f(b):
            u(a,b)
            cost += c
    ans.append(cost)
for i in range(1,testcase+1):
    print(f'Case #{i}: {ans[i-1]} meters')