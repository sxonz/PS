n = int(input())
d = list(map(int,input().split())) + [0]
n += 1
stack = []
m = 0
for i in range(n):
    r = d[i]
    while stack and stack[-1][1] > r:
        idx,v = stack.pop()
        if stack:
            day = i - stack[-1][0]-1
        else:
            day = i
        m = max(m,day*v)
    stack.append((i,r))
print(m)