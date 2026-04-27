import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = set(input().split()[1:])
party = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for p in party:
        if p & d:
            d = d.union(p)

cnt = 0
for party in party:
    if party & d:
        continue
    cnt += 1

print(cnt)