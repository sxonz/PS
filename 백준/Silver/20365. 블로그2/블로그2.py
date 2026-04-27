from collections import deque
n = int(input())
s = deque(input())
cnt = 0
while s:
    a = s[0]
    cnt += 1
    while s and s[0] == a:
        s.popleft()
    while s and s[-1] == a:
        s.pop()
print(cnt)

