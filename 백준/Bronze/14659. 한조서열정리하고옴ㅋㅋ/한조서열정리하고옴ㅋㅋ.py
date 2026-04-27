n = int(input())
d = list(map(int,input().split()))
r = 0
cur = 0
ans = 0
for i in d:
    if r > i:
        cur += 1
        ans = max(ans,cur)
    else:
        cur = 0
        r = i
print(ans)
         