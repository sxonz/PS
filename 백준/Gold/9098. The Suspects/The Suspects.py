ans = []
while True:
    n,m = map(int,input().split())
    if [n,m] == [0,0]:
        break
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
    for i in range(m):
        d = list(map(int,input().split()))
        l = d[0]
        for j in range(2,l+1):
            U(d[j-1],d[j])
    ans.append([F(i) for i in range(n)].count(0))
for i in ans:
    print(i)