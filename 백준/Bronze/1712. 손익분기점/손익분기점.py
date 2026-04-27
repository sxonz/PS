import math
a,b,c = map(int,input().split())
if b >= c:
    print(-1)
else:
    tmp = c-b
    res = math.floor(a/tmp)
    if tmp*res <= a:
        res += 1
    print(res)