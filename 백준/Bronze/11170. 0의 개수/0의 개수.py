prefix_sum = [0,1]
for i in range(1,1000001):
    prefix_sum.append(prefix_sum[-1]+str(i).count('0'))
for _ in range(int(input())):
    a,b = map(int,input().split())
    print(prefix_sum[b+1]-prefix_sum[a])