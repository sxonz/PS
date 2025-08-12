stack = []
result = ''
cnt = 0
for i in input()+' ':
    if i == '<' :
        cnt = 1
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)
    
    if i == '>' :
        cnt = 0
        for _ in range(len(stack)):
            result += stack.pop(0)

    if i == ' ' and not cnt:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
print(result)