s = input()[::-1]

flag = False
o = 0

d = [[0,0] for i in range(50)]
for i in s:
    if i.isdigit():
        if flag:
            d[o][0] *= int(i)
            flag = False
        else:
            d[o][0] += 1
    elif i == ")":
        d[o] = [0,sum(d[o])]
        o += 1
    else:
        d[o-1][0] += sum(d[o])
        d[o] = [0,0]
        o -= 1
        flag = True
print(sum(d[0]))