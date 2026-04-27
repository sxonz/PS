n,m=map(int,input().split())
d=[0]*n
for _ in range(m):
    a,b,c = map(int,input().split())
    for i in range(a-1,b):d[i] = c
print(*d)