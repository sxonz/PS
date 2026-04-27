n,k = map(int,input().split())
d = list(input())
stack = []
res = ''
flag = True
for i in d:
    if flag:
        if not stack:
            stack.append(i)
        else:
            while stack and int(stack[-1]) < int(i) and k:
                stack.pop()
                k -= 1
            stack.append(i)
            if not k:
                flag = False
    else:
        stack.append(i)
if k:
    stack = stack[:-k]
print(''.join(stack))