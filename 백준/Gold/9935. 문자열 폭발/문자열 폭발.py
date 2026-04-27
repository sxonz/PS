s = input()
n = len(s)
exp = list(input())
e = len(exp)
stack = []
for i in range(n):
    stack.append(s[i])
    while len(stack) >= e and stack[-e:] == exp:
        for k in range(e):
            stack.pop()
if not stack:
    print("FRULA")
else:
    print(''.join(stack))