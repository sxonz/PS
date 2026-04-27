n = int(input())
d = list(map(int,input().split())) + [0]
prefix_sum = [0]
for i in d:
    prefix_sum.append(prefix_sum[-1] + i)
n += 1
stack = []
m = 0
s,e = 0,0
for i in range(n):
    r = d[i]
    while stack and stack[-1][1] > r:
        idx,v = stack.pop()
        if stack:
            l = stack[-1][0] + 1
        else:
            l = 0
        if (prefix_sum[i]-prefix_sum[l])*v > m:
            m = (prefix_sum[i]-prefix_sum[l])*v
            s,e = l+1,i
    stack.append((i,r))
if not m:
    s,e = 1,1
print(m)
print(s,e)