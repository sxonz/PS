n = int(input())
d = list(map(int,input().split()))
maxv = 0
ans = 0
for i in d[::-1]:
    if i < maxv:
        ans += maxv-i
    else:
        maxv = i
print(ans)
