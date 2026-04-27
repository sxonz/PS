from itertools import permutations,combinations_with_replacement

n,m = map(int,input().split())
nums = list(map(int,input().split()))
temp = nums
for i in temp:
    if temp.count(i) == 1:
        nums.append(i)

d = sorted(list(set(combinations_with_replacement(sorted(nums),m))))
for i in d:
    i = [str(j) for j in i]
    print(' '.join(i))