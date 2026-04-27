testcase = int(input())
d = []
p_sum = [0,2]
for _ in range(testcase):
    a,b = map(int,input().split())
    d.append(b)
for num in range(2,max(d)+1):
    n = num
    res = n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            n //= i
            while n % i == 0:
                n //= i
            res *= ((i-1)/i)
    if n >= 2:
        res *= 1-(1/n)
    p_sum.append(int(p_sum[-1]+res))

for i in range(testcase):
    print('{0} {1}'.format(i+1,p_sum[d[i]]))