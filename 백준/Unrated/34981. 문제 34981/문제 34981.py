x,y = map(int,input().split())
n = int(input())
d = [0]*1440
for i in range(n):
    a,b,c = map(int,input().split())
    t = a*60+b
    while t<1440:
        d[t] =1
        t += c
def r(z):
    return '0'*(2-len(str(z)))+str(z)
for i in range(x*60+y,1440):
    if d[i]:
        print(r(i//60),":",r(i%60),sep='')
        break
else:
    for i in range(1440):
        if d[i]:
            print(r(i//60),":",r(i%60),sep='')
            break