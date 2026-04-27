s = input()
rev = {')':'(',']':'['}
m= {'(':2,')':2,'[':3,']':3}
mult = 1
ans = 0
flag = True

stack = []
for i in s:
    if i == '(' or i == '[':
        stack.append(i)
        mult *= m[i]
        flag = True
    else:
        if stack and stack[-1] == rev[i]:
            stack.pop()
            if flag:
                ans += mult
                flag = False
            mult //= m[i]
        else:
            print(0)
            break
else:
    ans = ans if not stack else 0
    print(ans)
        
    