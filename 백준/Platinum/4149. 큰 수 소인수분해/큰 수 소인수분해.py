from heapq import *
from random import randrange
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
def power(x,y,p):
    if y<2 : return (x**y)%p
    return (power(x,y//2,p)**2)%p if not y%2 else (x*power(x,y//2,p)**2)%p
def m_r(n,a):
    s,d=0,n-1
    while d%2 == 0:
        s+=1
        d//=2
    x = power(a,d,n)
    if x==1 or x==n-1: return True
    for i in range(s-1):
        x=power(x,2,n)
        if x+1==n:return True
    return False
def isprime(n):
    if n in P:return True
    if n==1 or n%2 == 0:return False
    for p in P:
        if not m_r(n,p):return False
    return True
def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b != 0:
        a,b=b,a%b
    return a
def rho(num):
    if isprime(num):return num
    if num%2 == 0:return 2
    x,c,d = randrange(2,num),randrange(1,num),1
    y=x
    while d == 1:
        x = ((x**2%num)+c)%num
        y = ((y**2%num)+c)%num
        y = ((y**2%num)+c)%num
        d = gcd(num,abs(x-y))
    return d if isprime(d) else rho(d)

n = int(input())
div = []
while n != 1:
    tmp = rho(n)
    n //= tmp
    heappush(div,tmp)
while div:
    print(heappop(div))