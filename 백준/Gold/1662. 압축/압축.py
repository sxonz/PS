s = input()[::-1]

flag = False
o = 0

d = [[0,0] for i in range(50)]
for i in s:
    if i == ")":
        d[o] = [0,d[o][0] + d[o][1]]
        o += 1
    elif i == "(":
        d[o-1][0] += d[o][0] + d[o][1]
        d[o] = [0,0]
        o -= 1
        flag = True
    else:
        if flag:
            d[o][0] *= int(i)
            flag = False
        else:
            d[o][0] += 1
print(d[0][0] + d[0][1])