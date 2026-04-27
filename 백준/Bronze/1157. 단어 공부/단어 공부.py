s = input().upper()
d = [0]*100

for i in s:
    d[ord(i)] += 1
m = max(d)
if d.count(m) >= 2:
    print('?')
else:
    print(chr(d.index(m)))