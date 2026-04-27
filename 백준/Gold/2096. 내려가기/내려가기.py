from collections import deque

n = int(input())

d = list(map(int,input().split()))
queue = deque([d[0],d[1],d[2]])
queue2 = deque([d[0],d[1],d[2]])
for i in range(1,n):
    d = list(map(int,input().split()))
    a,b,c = queue.popleft(),queue.popleft(),queue.popleft()
    queue.append(max(a,b)+d[0])
    queue.append(max(a,b,c)+d[1])
    queue.append(max(b,c)+d[2])
    a,b,c = queue2.popleft(),queue2.popleft(),queue2.popleft()
    queue2.append(min(a,b)+d[0])
    queue2.append(min(a,b,c)+d[1])
    queue2.append(min(b,c)+d[2])
print(max(queue),min(queue2))