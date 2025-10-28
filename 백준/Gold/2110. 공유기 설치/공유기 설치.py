import sys
input = sys.stdin.readline

n,c = map(int,input().split())
d = [int(input()) for i in range(n)]
d.sort()

x = d[-1]
l,r = 0,x-d[0]
while l<r:
    mid = (l+r)//2
    flag = False
    end = -1
    cnt = 0
    for i in d:
        if i > end:
            end = i+mid
            cnt += 1
            if cnt == c:
                flag = True
                break
            if end >= x:
                break
    if flag:
        l = mid+1
    else:
        r = mid
print(r)


