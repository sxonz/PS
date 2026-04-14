from collections import deque

a, b, s = map(int, input().split())
q = deque([])

def gcd(n, m, T):
    if not m:return n
    if T:q.appendleft(n // m)
    return gcd(m, n % m,T)

P = 1

if not a+b:
    if s: P = 0
elif not a:
    if s % b:P = 0
elif not b:
    if s % a:
        P = 0
else:
    g = gcd(a, b,True)
    if s % g != 0:
        P = 0
    else:
        x, y = 1, 0
        for div in q:
            x, y = y, x - y * div
        x *= s // g
        y *= s // g
        
        divx = b // g
        divy = a // g
        if x <= 0:
            tmp = -x // divx + 1
            x += tmp * divx
            y += -tmp * divy
        if x > divx:
            tmp = x // divx
            if x % divx == 0:
                tmp += 1
            x -= tmp * divx
            y += tmp * divy
        if a * x + b * y != s:P = False
        while y > 0:
            if gcd(x,y,False)==1:break
            x += divx;y -= divy
        else:P = 0
res='YES'if P or a==s or b==s else'NO'
print(res)