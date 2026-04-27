n = int(input())
d = [i*2+1 for i in range(0,50001)]
prefix_sum = [d[0]]
for i in d[1:]:
    prefix_sum.append(prefix_sum[-1]+i)
p1,p2 = 0,1
cnt = 0
d = []
while p2 < len(prefix_sum):
    if prefix_sum[p2] - prefix_sum[p1] == n:
        d.append(prefix_sum[p2])   
        p1 += 1
        p2 += 1
    elif prefix_sum[p2] - prefix_sum[p1] < n:
        p2 += 1
    else:
        p1 += 1
for i in d:
    print(int(i**0.5))
if not d:
    print(-1)