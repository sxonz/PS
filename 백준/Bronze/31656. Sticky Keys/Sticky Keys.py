s = input()
res = ''
bef = ''
for i in s:
    if i != bef:
        res += i
    bef = i
print(res)