res = []
while True:
    n,l = map(int,input().split())
    if (n,l) == (0,0):
        break
    loop = []
    while n not in loop:
        loop.append(n)
        for i in range(l-len(str(n))):
            n *= 10
        n,n2 = ''.join(sorted(str(n),reverse=True)),''.join(sorted(str(n)))
        n = int(n)-int(n2)
    res.append([loop.index(n),n,len(loop)-loop.index(n)])
for i in res:
    print(i[0],i[1],i[2])