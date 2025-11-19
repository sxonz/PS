n = int(input())
d = list(map(int,input().split()))
cur = [0]*1000002
ans = n
for i in d:
    if cur[i+1]:
        cur[i+1] -= 1
        ans -= 1
    cur[i] += 1
print(ans)