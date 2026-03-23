x,y = map(int,input().split())
a = (x+y)//2
b = x-a
if a+b != x or abs(a-b) != y or a<0 or b<0:
    print(-1)
else:
    print(a,b)