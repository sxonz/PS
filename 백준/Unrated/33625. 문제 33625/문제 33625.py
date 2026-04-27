n = int(input())
d = list(map(int,input().split()))
flag = False
for i in d:
    if not i:
        flag = True
if flag:
    cnt = sum([1 for x in d if not x])
    print(n-cnt)
else:
    g = d[0]
    for x in d[1:]:
        g &= x
    if g != 0:
        print(-1)
    else:
        m = n+1
        for i in range(n):
            cur = d[i]
            for j in range(i,n):
                cur &= d[j]
                if not cur:
                    m = min(m,j-i+1)
                    break
        print((m-1) + (n-1))
