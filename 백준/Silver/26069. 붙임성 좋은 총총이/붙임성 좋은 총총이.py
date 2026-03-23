n = int(input())
d = dict()
d["ChongChong"] = 1
for i in range(n):
    a,b = input().split()
    if a not in d:
        d[a] = 0
    if b not in d:
        d[b] = 0
    if d[a] or d[b]:
        d[a] = 1
        d[b] = 1
print(sum(d.values()))