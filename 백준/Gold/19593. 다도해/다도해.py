testcase = int(input())
ans = []
d = [list(map(int,input().split())) for t in range(testcase)]
for n,seed,a,b in d:
    pn = n**2
    p = list(range(n))
    def F(x):
        if x != p[x]: p[x] = F(p[x])
        return p[x]
    def U(a,b):
        a,b = F(a),F(b)
        if a<b:
            p[b] = a
        else:
            p[a] = b

    e = set([seed % pn])
    tmp = seed % pn
    day = 1
    U(tmp//n,tmp%n)
    while len(set(p)) != 1:
        tmp = (tmp * a + b) % pn
        if tmp in e:
            day = 0
            break
        e.add(tmp)
        day += 1
        x,y = divmod(tmp,n)
        U(x,y)
        for i in range(n):
            F(i)
    ans.append(day)
for i in ans:
    print(i)