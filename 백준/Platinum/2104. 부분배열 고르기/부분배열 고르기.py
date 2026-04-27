n = int(input())
n += 1
d = list(map(int,input().split())) + [0]
prefix_sum = [0,d[0]]
for i in range(1,n):
    prefix_sum.append(prefix_sum[-1] + d[i])

m = 0
stack = []
for i in range(n):
    r = d[i]
    while stack and stack[-1][1] > r:
        idx,v = stack.pop()
        if stack:
            idx = stack[-1][0] + 1
        else:
            idx = 0
        e = i
        m = max(m,(prefix_sum[e]-prefix_sum[idx]) * v)
    stack.append((i,r))
print(m)