from math import *
MOD = int(1e9)+7
for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    d.sort(reverse=True)
    ans = 1
    if d[-1]:
        print(1)
        continue
    for i in d:
        ans = (ans * comb(n,i))%MOD
        n -= i
    print(ans)