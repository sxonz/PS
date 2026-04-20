n = int(input())
d = list(map(int,input().split()))

path = [1]
stack = []
for i in range(n-1):
    while stack and stack[-1][0] >= d[i]:
        path.append(stack.pop()[1])
    stack.append((d[i],i+2))
for i in stack:
    path.append(i[1])
print(*(path))