from itertools import permutations

n,m = map(int,input().split())
nums = list(map(int,input().split()))
d = permutations(sorted(nums),m)
for i in d:
    i = [str(j) for j in i]
    print(' '.join(i))