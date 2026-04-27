
d = []
while True:
    d.append(int(input()))
    if d[-1] == 0:
        d.pop()
        break
for n in d:
    if n == 1:
        print(0)
        continue
    res = n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            n //= i
            while n % i == 0:
                n //= i
            res *= ((i-1)/i)
    if n >= 2:
        res *= 1-(1/n)
    print(int(res))