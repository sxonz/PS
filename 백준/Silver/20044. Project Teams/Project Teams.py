n = int(input())
d = list(map(int,input().split()))
d.sort()
m = int(1e9)
for i in range(n):
    m = min(m,d[i]+d[n*2-i-1])
print(m)