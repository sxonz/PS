from math import ceil

n = int(input())
d = list(map(int,input().split()))

prefix_sum = [0]
for k in 1,2:
    for i in d:
        prefix_sum.append(prefix_sum[-1] + i)

cnt = 0
s = prefix_sum[n]
for i in range(1,n+1):
    for j in range(i,i+n):
        r = prefix_sum[j] - prefix_sum[i]
        if r < 0:
            cnt += ceil(-r/s)

print(cnt)