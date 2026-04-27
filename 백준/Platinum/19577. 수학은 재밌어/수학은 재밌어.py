def div(n):

    divisors = []

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i) 
            if i**2 != n : 
                divisors.append(n // i)

    divisors.sort()
    
    return divisors

num = int(input())

for divisor in div(num):
    n = divisor
    res = n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            n //= i
            while n % i == 0:
                n //= i
            res *= ((i-1)/i)
    if n >= 2:
        res *= 1-(1/n)
    if int(res)*divisor == num:
        print(divisor)
        break
else:
    print(-1)