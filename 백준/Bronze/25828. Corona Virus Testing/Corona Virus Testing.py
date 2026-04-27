a,b,c = map(int,input().split())
d,e=a*b,b*c+a
if d<e:
    print(1)
elif e<d:
    print(2)
else:
    print(0)