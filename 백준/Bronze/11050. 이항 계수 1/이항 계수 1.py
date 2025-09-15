from itertools import combinations
n,k = map(int,input().split())
print(len(list(combinations(range(n),k))))