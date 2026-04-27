n,power = map(int,input().split())
d = []
a = []
cnt = 0
for i in range(n):
    r,p = map(int,input().split())
    if r == 2:
        a.append(p)
        cnt += 1
    else:
        d.append(p)
d.sort()
a.sort()
for i in d:
    while a and power <= i:
        power *= a.pop(0)
    if power > i:
        cnt += 1
        power += i
    else:
        break
print(cnt)