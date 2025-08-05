n = int(input())
d = dict()
for i in range(n):
    s,e = input().split(".")
    if e not in d:
        d[e] = 0
    d[e] += 1
for i in sorted(d.keys()):
    print(i,d[i])
