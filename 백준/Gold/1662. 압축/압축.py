s = input()[::-1]

r = 0
flag = False
o = 0

stack = [[0,0]]
for i in s:
    if i.isdigit():
        if flag:
            stack[-1][0] *= int(i)
            flag = False
        else:
            stack[-1][0] += 1
    elif i == ")":
        stack[-1] = [0,sum(stack[-1])]
        o += 1
        if len(stack) <= o:
            stack.append([0,0])
    else:
        stack[o-1][0] += sum(stack[o])
        stack.pop()
        o -= 1
        flag = True
print(sum(stack[0]))