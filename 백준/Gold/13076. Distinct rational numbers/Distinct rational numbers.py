import time
testcase = int(input())
d = [int(input()) for _ in range(testcase)]

phi = []
for n in range(1,10001):
    res = n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            n //= i
            while n % i == 0:
                n //= i
            res *= ((i-1)/i)
    if n >= 2:
        res *= 1-(1/n)
    phi.append(int(res))

prefix_sum = [0]
for i in phi:
    prefix_sum.append(prefix_sum[-1]+i)
for i in d:
    print(prefix_sum[i]+1)