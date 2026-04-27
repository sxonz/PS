s = input()
res = ""
op = "+-*/()"
priority = {"(":2,")":2,"*":1,"/":1,"+":0,"-":0}
operator = []
for i in s:
    if i not in op:
        res += i
        continue
    else:
        if i == "(":
            operator.append("(")
            continue
        if i == ")":
            while operator[-1] != "(":
                tmp = operator.pop()
                res += tmp
            operator.pop()
            continue
        if operator and operator[-1] != "(" and priority[operator[-1]] >= priority[i]:
            while operator and operator[-1] != "(" and priority[operator[-1]] >= priority[i]:
                res += operator.pop()
        operator.append(i)
while operator:
    tmp = operator.pop()
    if priority[tmp] < 2:
        res += tmp
print(res)