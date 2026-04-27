n = int(input())
d = list(map(int,input().split()))
stack = []
cur = 1
for i in d:
    while stack and stack[-1] == cur:
        cur += 1
        stack.pop()
    flag = True
    if i == cur:
        cur += 1
        flag = False
    while stack and stack[-1] == cur:
        cur += 1
        stack.pop()
    if flag:
        stack.append(i)
if cur == n+1:
    print("Nice")
else:
    print("Sad")