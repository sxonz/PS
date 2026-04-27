import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque([n + 1 for n in range(n)])

for _ in range(n - 1):
    q.popleft()
    q.append(q.popleft())
print(q.pop())