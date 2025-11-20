import sys
input = sys.stdin.readline
n = int(input())
d = [int(input()) for i in range(n)]
stack = []
ans = 0
for i in d:
    while stack and stack[-1] <= i:
        stack.pop()
    ans += len(stack)
    stack.append(i)
print(ans)
