n = int(input())
d = list(map(int,input().split()))
cur = 0
ans = 0
for i in d:
    if i == cur:
        ans += 1
        cur = (cur+1)%3
print(ans)