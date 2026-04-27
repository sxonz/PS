a,b = input().split()
n,m = len(a), len(b)
ans = int(1e9)
for i in range(m-n+1):
    tmp = 0
    for j in range(i,i+n):
        if a[j-i] != b[j]:
            tmp += 1
    ans = min(ans,tmp)
print(ans)