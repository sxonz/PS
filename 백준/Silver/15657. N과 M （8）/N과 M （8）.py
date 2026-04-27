from itertools import combinations_with_replacement

n,m = map(int,input().split())
nums = list(map(int,input().split()))
d = combinations_with_replacement(sorted(nums),m)
for i in d:
    i = [str(j) for j in i]
    print(' '.join(i))