n,m = map(int,input().split())
r = 1
for i in range(2,n+1):
    r = r * i % m
print(r%m)