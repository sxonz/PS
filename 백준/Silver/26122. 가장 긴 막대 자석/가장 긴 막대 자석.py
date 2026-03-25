n = int(input())
s = input()
bef = s[0]
cur = 0
r = []
for i in range(n):
    if s[i] == bef:
        cur += 1
    else:
        r.append(cur)
        cur = 1
    bef = s[i]
r.append(cur)
if len(r) > 1:
    print(2*max([min(r[i],r[i+1]) for i in range(len(r)-1)]))
else:
    print(0)