from math import *
for t in range(int(input())):
    k,n = map(int,input().split())
    d = list(map(int,input().split()))
    psum = [0]
    cnt = {0:1}
    for i in d:
        psum.append((psum[-1]+i)%k)
        if psum[-1] not in cnt:
            cnt[psum[-1]] = 0
        cnt[psum[-1]] += 1
    ans = 0
    for i in cnt:
        ans += comb(cnt[i],2)
    print(ans)