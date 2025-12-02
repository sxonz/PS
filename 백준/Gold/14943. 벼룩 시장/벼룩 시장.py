n = int(input())
d = list(map(int,input().split()))
stack = []
res = 0
for i in range(n):
    if d[i] > 0:
        while stack and stack[-1][0] < 0 and d[i]:
            if -stack[-1][0] > d[i]:
                stack[-1][0] += d[i]
                res += (i-stack[-1][1])*d[i]
                d[i] = 0
            else:
                x,idx = stack.pop()
                res += (i-idx)*-x
                d[i] += x       
        
    else:
        while stack and stack[-1][0] > 0 and d[i]:
            if stack[-1][0] > -d[i]:
                stack[-1][0] += d[i]
                res += (i-stack[-1][1])*-d[i]
                d[i] = 0
            else:
                x,idx = stack.pop()
                res += (i-idx)*x
                d[i] += x

    if d[i]:
        stack.append([d[i],i])
print(res)