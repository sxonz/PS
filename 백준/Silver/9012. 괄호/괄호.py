n = int(input())
d = []
rev = {')':'(',']':'['}
for i in range(n):
    d.append(input())
for i in d:
    stack = []
    for j in i:
        if j in ['(','[']:
            stack.append(j)
        elif j in [')',']']:
            if not stack or stack[-1] != rev[j]:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')