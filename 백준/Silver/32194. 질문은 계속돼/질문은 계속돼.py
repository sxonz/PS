import sys
input = sys.stdin.readline
n = int(input())
prefix_sum = [0,1]
for i in range(n):
    q,a,b = map(int,input().split())
    if q == 1:
        r = prefix_sum[b] - prefix_sum[a-1] == b-a+1
    else:
        r = prefix_sum[b] == prefix_sum[a-1]
    print("YNeos"[r^1::2])
    prefix_sum.append(prefix_sum[-1]+r)
