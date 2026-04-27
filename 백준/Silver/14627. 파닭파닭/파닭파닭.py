import sys
input = sys.stdin.readline

n,k = map(int,input().split())
d = [int(input()) for i in range(n)]
l,r = 0,max(d)+1
while l+1<r:
    mid = (l+r)//2
    cnt = 0
    for i in d:
        cnt += i//mid
        if cnt >= k:
            l = mid
            break
    else:
        r = mid
print(sum(d)-l*k)
    