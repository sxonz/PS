n,l = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()

pr=-1
wl=0

ans = 0
for s,e in d:
    e -= 1
    amount = (pr-wl+1)//l+bool((pr-wl+1)%l)
    ans += amount
    wl = max(wl+l*amount,s)
    pr = e
print(ans+(pr-wl+1)//l+bool((pr-wl+1)%l))
    