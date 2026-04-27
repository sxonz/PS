import sys
input = sys.stdin.readline
n,h = map(int,input().split())
tmp = [int(input()) for _ in range(n)]
up_sum = [0]*(h)
down_sum = [0]*(h)
for i,j in zip(tmp[::2],tmp[1::2]):
    up_sum[i-1] += 1
    down_sum[j-1] += 1
for i in range(h-1,0,-1):
    up_sum[i-1] += up_sum[i]
    down_sum[i-1] += down_sum[i]
d = [i+j for i,j in zip(up_sum,down_sum[::-1])]
m = min(d)
print(m,d.count(m))