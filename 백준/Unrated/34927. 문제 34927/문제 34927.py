n = int(input())
d = list(map(int,input().split()))
d.sort()
ans = 0
cur = 0
for i in d:
    if cur <= i:
        cur += i
        ans += 1
print(ans)