n = int(input())
stack = []
ans = []
d = [int(input()) for _ in range(n)]
idx = 1
didx = 0

while idx <= n or (stack and stack[-1] == d[didx]):
    if stack and stack[-1] == d[didx]:
        stack.pop()
        ans.append("-")
        didx += 1
    elif idx <= n:
        stack.append(idx)
        ans.append("+")
        idx += 1
    else:
        break

if stack:
    print("NO")
else:
    print("\n".join(ans))
