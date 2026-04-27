n = input()

s = input()
d = dict()

for i in s:
    if 97 <= ord(i) <= 122:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
print(max(d.values()))