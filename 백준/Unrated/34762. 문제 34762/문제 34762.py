n,k = map(int,input().split())
s = int(input())
d = list(map(int,input().split()))
flag = d[-1] == n or d[-1] < n-k
for i in range(1,s):
    if d[i] - 1 == d[i-1]:
        continue
    flag &= d[i]-k-1 > d[i-1]
print("YES" if flag else "NO")
