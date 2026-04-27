num = int(input())

d = []
for n in range(1,num+1):
    res = n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            n //= i
            while n % i == 0:
                n //= i
            res *= ((i-1)/i)
    if n >= 2:
        res *= 1-(1/n)
    d.append(int(res))
print(sum(d)-1)