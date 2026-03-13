from math import *
MAX = 1000001
p = []
prime = [1]*MAX
for i in range(2,MAX):
    if prime[i]:
        p.append(i)
        if i < int(MAX**0.5+1):
            k = 2
            while i*k<MAX:
                prime[i*k] = 0
                k += 1

n = int(input())

tmp = 0
for i in p:
    while n%i == 0:
        n //= i
        tmp += 1
if n>1:
    tmp += 1

print(ceil(log2(tmp)))