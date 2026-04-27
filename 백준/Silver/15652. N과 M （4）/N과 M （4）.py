from itertools import combinations_with_replacement

n,m = map(int,input().split())
d = combinations_with_replacement(range(1,n+1),m)
for i in d:
    i = [str(j) for j in i]
    print(' '.join(i))