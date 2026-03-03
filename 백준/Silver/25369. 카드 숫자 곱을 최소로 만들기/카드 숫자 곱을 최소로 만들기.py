from itertools import combinations_with_replacement
n = int(input())
MAX = 9**n+1
tmp = list(map(int,input().split()))
cur = 1
for i in tmp:
    cur *= i

ans = MAX
d = [MAX]*n
for i in combinations_with_replacement(range(1,10),n):
    m = 1
    t = []
    for j in i:
        m *= j
        t.append(j)
    if cur>=m:
        continue

    t.sort()
    if t < d:
        d = t[::]
        ans = m
if ans == MAX:
    print(-1)
else:
    print(*d)