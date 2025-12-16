n,m,k = map(int,input().split())
if n+m-1 > k:
    print("NO")
    exit()
print("YES")
for i in range(n):
    print(*range(i+1,i+1+m))
    