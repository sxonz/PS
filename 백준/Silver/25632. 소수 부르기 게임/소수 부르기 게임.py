def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True
a,b=map(int,input().split())
c,d=map(int,input().split())
x,y,z=[],[],[]
for i in range(a,b+1):
    if check(i):x.append(i)
for j in range(c,d+1):
    if check(j):y.append(j)
    if j in x:
        z.append(j)
u=set()
while True:
    if not x:
        print('yj')
        break
    if z:
        u.add(z.pop())
    else:
        while x:
            t=x.pop()
            if t not in u:
                u.add(t)
                break
        else:
            print('yj')
            break
    if not y:
        print('yt')
        break
    if z:
        u.add(z.pop())
    else:
        while y:
            t=y.pop()
            if t not in u:
                u.add(t)
                break
        else:
            print('yt')
            break