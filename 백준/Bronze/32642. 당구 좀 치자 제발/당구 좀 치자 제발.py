n = int(input())
ans = 0
cur = 0
for i in map(int,input().split()):
    cur += i*2-1
    ans += cur
print(ans)
    