fac = [1]
l = 1
def F(n):
    global l
    i = len(fac)
    while i <= n:
        fac.append(l := l*i)
        i += 1
    return fac[n]

n,m,k = map(int,input().split())

if k:
    n1 = (k-1)//m
    m1 = k - n1*m - 1
    n2 = n - n1 - 1
    m2 = m - m1 - 1
    f = (F(n1+m1)//(F(n1)*F(m1)))
    s = (F(n2+m2)//(F(n2)*F(m2)))
    print(f*s)
else:
    print((F(n+m-2)//(F(n-1)*F(m-1))))