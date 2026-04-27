testcase = int(input())
res = [[] for _ in range(testcase)]
for t in range(testcase):
    n,k = int(input()),int(input())
    p = list(range(n))
    def F(x):
        if x-p[x]:p[x] = F(p[x])
        return p[x]
    for i in range(k):
        a,b = map(int,input().split())
        a,b = F(a),F(b)
        if a<b:
            p[b] = a
        else:
            p[a] = b
    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        r = 0 if F(a)-F(b)else 1
        res[t].append(r)
for i in range(testcase):
    if i:print()
    print(f"Scenario {i+1}:")
    for j in res[i]:
        print(j)