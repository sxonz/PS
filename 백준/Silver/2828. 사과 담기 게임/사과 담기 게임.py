n,m = map(int,input().split())
d = [int(input()) for i in range(int(input()))]
l,r = 1,m
ans = 0
for i in d:
    if i>r:
        ans += i-r
        l += i-r
        r += i-r
    elif i<l:
        ans += l-i
        r -= l-i
        l -= l-i
print(ans)

