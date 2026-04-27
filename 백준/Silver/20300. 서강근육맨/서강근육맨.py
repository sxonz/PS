n = int(input())
d = list(map(int,input().split()))
m = 0
d.sort()
if n%2:
    m = d[-1]
    n -= 1
for i in range(n//2):
    m = max(m,d[i]+d[n-i-1])
print(m)