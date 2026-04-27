n,m = map(int,input().split())
m -= 1
for i in range(n-m):
    print(i,i+1)
r = n-m-1
for i in range(n-m+1,n):
    print(r,i)