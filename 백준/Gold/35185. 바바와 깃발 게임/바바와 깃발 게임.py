n,k = map(int,input().split())
s = input()
l,r = 0,0
cur = 0
ridx = 0
lidx = 0
for id,i in enumerate(s):
    if i == "L":
        cur -= 1
    else:
        cur += 1
    if cur < l:
        l = cur
        lidx = id
    if cur > r:
        r = cur
        ridx = id

if (k-1 not in [lidx,ridx]) or -l+r+1 > n:
    print("DEFEAT")
else:
    print("WIN")
    if ridx == k-1:
        print(-l+1,-l+r+1)
    else:
        print(n-r,n-r+l)