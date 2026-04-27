def p(num):
    prime = [True]*(num+1)
    prime[0],prime[1] = False,False
    for i in range(2,int(num**0.5)+1):
        if prime[i]:
            k = 2
            while i*k <= n:
                prime[i*k] = False
                k += 1
    res = []
    for i in range(len(prime)):
        if prime[i]:
            res.append(i)
    return res

n = int(input())

d = p(n)
d.insert(0,0)
prefix_sum = [0]
for i in range(1,len(d)):
    prefix_sum.append(prefix_sum[-1]+d[i])
cnt = 0
p1,p2 = 0,1
while len(prefix_sum) > p2 > p1:
    if prefix_sum[p2]-prefix_sum[p1] == n:
        cnt += 1
        p2 += 1
    elif prefix_sum[p2]-prefix_sum[p1] < n:
        p2 += 1
        p1 -= 1
    p1 += 1

print(cnt)