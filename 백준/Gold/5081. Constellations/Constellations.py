ans = []
while True:
    n = int(input())
    if not n:
        break
    d = [tuple(map(int,input().split())) for _ in range(n)]
    p = list(range(n))
    def F(x):
        if x-p[x]:p[x] = F(p[x])
        return p[x]
    def U(a,b):
        a,b = F(a),F(b)
        if a<b:
            p[b] = a
        else:
            p[a] = b
    for i in range(n):
        m = int(1e10)
        for j in range(n):
            if i==j:
                continue
            m = min(m,((d[i][0]-d[j][0])**2 + (d[i][1]-d[j][1])**2))
        for j in range(n):
            if ((d[i][0]-d[j][0])**2 + (d[i][1]-d[j][1])**2) == m:
                U(i,j)

    ans.append([F(i) for i in range(n)])
for i in range(len(ans)):
    print(f"Sky {i+1} contains {len(set(ans[i]))} constellations.")