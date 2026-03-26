n = int(input())
d = list(map(int,input().split()))
d.sort(reverse=True)
e = -1
ans = 0
for i in range(n):
    e = max(e,i+d[i]-1)
    if e >= i:
        ans += 1
print(ans)
