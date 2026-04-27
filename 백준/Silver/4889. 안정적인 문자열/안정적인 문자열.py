test = 1
while True:
    stack = []
    count = 0
    s = input()

    if s[0] == '-':
        break

    for i in s:
        if i == "{":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                count+=1
                stack.append('{')
    
    print(f'{test}. {count+len(stack)//2}')
    test+=1