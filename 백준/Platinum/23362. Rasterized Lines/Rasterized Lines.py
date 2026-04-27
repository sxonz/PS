from collections import deque
from random import randrange
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
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
    if n == 1 or n%2 == 0:return False
    for p in P:
        if not m_r(n, p):return False
    return True
def gcd(a,b):
    a, b=max(a, b), min(a, b)
    while b != 0:
        a, b=b, a%b
    return a
def rho(num):
    if isprime(num): return num
    if num%2 == 0: return 2
    x,c,d = randrange(2,num), randrange(1,num), 1
    y=x
    while d == 1:
        x = ((x**2%num)+c) % num
        y = ((y**2%num)+c) % num
        y = ((y**2%num)+c) % num
        d = gcd(num, abs(x-y))
    return d if isprime(d) else rho(d)
def phi(n):
    res = n
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            n //= i
            while n % i == 0:
                n //= i
            res *= ((i-1)/i)
    if n >= 2:
        res *= 1-(1/n)
    return int(res)

def solve(n):
    r = n
    div = []
    while n > 1:
        tmp = rho(n)
        div.append(tmp)
        n //= tmp
    queue = deque([r])
    d = [r]
    while queue:
        x = queue.popleft()
        for i in div:
            if x%i == 0:
                if x//i not in d:
                    queue.append(x//i)
                    d.append(x//i)
    ans = 0
    for i in d:
        ans += phi(r/i+1)
    return ans
testcase = int(input())
vxeuuq=[]
for _ in range(testcase):
    input()
    test = int(input())
    vxeuuq.append(solve(test))
for i in vxeuuq:
    print(i)