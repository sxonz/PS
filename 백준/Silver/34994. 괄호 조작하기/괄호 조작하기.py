r = "()[]{}"
rev = {")":"(","}":"{","]":"["}
for t in range(int(input())):
    s = list(input())
    n = len(s)
    comp = False
    for j in range(n):
        if comp:
            break
        tmp = s[::]
        for k in range(6):
            tmp[j] = r[k]
            stack = []
            flag = True
            for i in tmp:
                if i in "([{":
                    stack.append(i)
                else:
                    if not stack:
                        flag = False
                        break
                    if stack[-1] != rev[i]:
                        flag = False
                        break
                    stack.pop()
            else:
                if stack:
                    flag = False
                else:
                    if tmp[j] == s[j]:
                        print("YES",0)
                        comp = True
                        break
                    else:
                        print("YES",1)
                        print(j+1,r[k])
                        comp = True
                        break
    if not comp:
        print("NO")
            



