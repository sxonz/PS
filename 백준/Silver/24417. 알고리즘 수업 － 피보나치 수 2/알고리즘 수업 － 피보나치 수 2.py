n = int(input())
bbef = 0
bef = 1
cur = 1
for i in range(n-1):
    cur = (bef+bbef) % 1000000007
    bbef = bef
    bef = cur
print(cur,n-2)