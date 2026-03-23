d = dict()
for i in range(int(input())):
    s,q = input().split()
    if q == "enter":
        d[s] = 1
    else:
        d[s] = 0
for i in sorted(d,reverse=True):
    if d[i]:
        print(i)