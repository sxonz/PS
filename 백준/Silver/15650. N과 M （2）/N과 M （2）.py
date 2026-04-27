from itertools import combinations
n,m = map(int,input().split())
d = list(combinations(range(1,n+1),m))
for i in d:
    j = [str(tmp) for tmp in i]
    print(' '.join(j))