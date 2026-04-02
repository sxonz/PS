h,n = map(int,input().split())
d = list(map(int,input().split()))
ans = 0
stack = []
maxv = 0
for i in range(n):
    maxv = max(maxv,d[i])
    tmp = 1
    while stack and stack[-1][0] < d[i]:
        r = stack.pop()
        ans += r[2]*(min(d[i],r[1])-r[0])
        tmp += r[2]
    stack.append((d[i],maxv,tmp))
print(ans)