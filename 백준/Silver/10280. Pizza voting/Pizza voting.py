from collections import deque
n,k = map(int,input().split())
d = deque(range(1,n+1))
oper = {0:1,1:2,2:0}
o = 0
for i in range(n-1):
    if o == 0:
        r = d.pop()
    elif o == 1:
        r = d.popleft()
    else:
        if k-d[0] >= d[-1]-k:
            r = d.popleft()
        else:
            r = d.pop()
    if r == k:
        print("NO")
        break
    o = oper[o]
else:
    print("YES")
