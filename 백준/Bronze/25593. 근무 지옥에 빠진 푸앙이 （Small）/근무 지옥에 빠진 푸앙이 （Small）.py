n = int(input())
d = dict()

for i in range(n):
    for j in 4,6,4,10:
        for k in input().split():
            if k != '-':
                if k not in d:
                    d[k] = 0
                d[k] += j
if not d:
    print("Yes")
else:
    print("YNeos"[max(d.values())-min(d.values())>12::2])