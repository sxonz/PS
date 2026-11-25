from collections import deque

d = [deque(map(int,input())) for i in range(4)]
d = [deque([0,0,0,0,0,0,0,0])] + d + [deque([0,0,0,0,0,0,0,0])]

k = int(input())
for i in range(k):
    a,b = map(int,input().split())
    r = [(a,b)]
    i = a
    cur = b
    while i < 5 and d[i][2] != d[i+1][6]: 
        cur = (cur-1)*-1-1
        r.append((i+1,cur))
        i += 1 
    i = a
    cur = b
    while i > 0 and d[i][6] != d[i-1][2]: 
        cur = (cur-1)*-1-1
        r.append((i-1,cur))
        i -= 1 
    for a,b in r:
        d[a].rotate(b)
ans = 0
for i in range(1,5):
    if d[i][0] == 1:
        ans += 2**(i-1)

print(ans)


