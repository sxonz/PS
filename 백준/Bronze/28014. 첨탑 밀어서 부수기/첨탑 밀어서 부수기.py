n = int(input())
ans = 0
bef = -1
for i in list(map(int,input().split())):
    if i>=bef:
        ans += 1
    bef = i
print(ans)