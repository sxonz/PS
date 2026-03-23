from collections import deque
n = int(input())
r = list(map(int,input().split()))
d = list(map(int,input().split()))
queue = deque([d[i] for i in range(n) if not r[i]])
q = int(input())
ans = []
for i in list(map(int,input().split())):
    queue.appendleft(i)
    ans.append(queue.pop())
print(*ans)