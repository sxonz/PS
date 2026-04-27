from itertools import combinations

n,m = map(int,input().split())
p = list(map(int,input().split()))
res = 0
for i in range(1,n+1):
    for comb in combinations(p,i):
        temp = 1
        for x in comb:
            temp *= x     
        res += (-1)**((i%2)^1)*(m // temp)
print(res)