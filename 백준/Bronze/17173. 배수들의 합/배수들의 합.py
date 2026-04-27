n,m = map(int,input().split())
d = [0]*(n+1)
r = list(map(int,input().split()))
for i in r:
    k = 1
    while i*k <= n:
        d[i*k] = i*k
        k += 1
print(sum(d))