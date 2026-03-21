n = int(input())
d = [input() for i in range(n)]

ans = 0
for i in d:
    stack = []
    for j in i:
        if stack and stack[-1] == j:
            stack.pop()
        else:
            stack.append(j)
    if not stack:
        ans += 1
print(ans)