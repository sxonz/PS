s = input()
d = dict()
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
cnt = 0
for i in d.values():
    if i%2:cnt += 1
print(max(0,cnt-1))