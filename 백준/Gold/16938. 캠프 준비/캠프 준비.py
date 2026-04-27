from itertools import combinations

n,l,r,x = map(int,input().split())
d = list(map(int,input().split()))
ans = 0
for i in range(2,n+1):
    for j in combinations(d,i):
        if l <= sum(j) <= r and max(j) - min(j) >= x:
            ans += 1
print(ans)