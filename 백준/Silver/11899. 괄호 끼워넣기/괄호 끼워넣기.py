s = input()
c = 0
res = 0
for i in s:
    if i == ')':
        if not c:
            res += 1
        else:
            c -= 1
    else:
        c += 1
print(res+c)