a=sum(list(map(int,input().split())))
b=sum(list(map(int,input().split())))
c=sum(list(map(int,input().split())))
d=sum(list(map(int,input().split())))
e=sum(list(map(int,input().split())))
tmp=[a,b,c,d,e]
if max(tmp) == a:
    print(1,a)
elif max(tmp) == b:
    print(2,b)
elif max(tmp) == c:
    print(3,c)
elif max(tmp) == d:
    print(4,d)
elif max(tmp) == e:
    print(5,e)