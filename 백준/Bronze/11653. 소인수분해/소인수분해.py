n = int(input())
prime = [1]*(n+1)
p = []
for i in range(2,n+1):
    if prime[i]:
        p.append(i)
        if i < int(n**0.5+1):
            k = 2
            while i*k <= n:
                prime[i*k] = 0
                k += 1
for i in p:
    while n%i == 0:
        print(i)
        n //= i
if n > 1:
    print(n)
