from collections import deque
n=int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()
rope = deque(rope)
m=0
while n:
    m = max(m,n*rope[0])
    n -= 1
    rope.popleft()

print(m)