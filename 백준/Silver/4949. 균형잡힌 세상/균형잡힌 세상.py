rev = {')':'(',']':'[',}
while True:
    s = input()
    if s == '.':
        break
    stack = []
    for i in s:
        if i in ['(','[']:
            stack.append(i)
        elif i in [')',']']:
            if not stack or stack[-1] != rev[i]:
                print('no')
                break
            else:
                stack.pop()
    else:
        if not stack:
            print('yes')
        else:
            print('no')
