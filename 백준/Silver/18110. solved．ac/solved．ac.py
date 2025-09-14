round = lambda x: int(x) + 1 if (x-int(x)) >= 0.5 else int(x)
n = int(input())
d = sorted([int(input()) for i in range(n)])
for i in range(r:=round(n*15/100)):
    d.pop()
d = d[r:]
if not d:
    print(0)
    exit(0)
print(round(sum(d)/len(d)+0.00001))