d = dict()
for i in range(int(input())):
    s = input()
    if s not in d:
        d[s] = 0
    d[s] += 1
m = 0
s = ''
for i in sorted(d.keys()):
    if d[i] > m:
        m = d[i]
        s = i
print(s)