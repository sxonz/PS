a,b = map(int,input().split())
c,d = map(int,input().split())
x,y = -a+b,-c+d
while x!=y:
    if x<y:
        x += b
    else:
        y += d
print(x)