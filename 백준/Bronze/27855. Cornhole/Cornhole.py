a,b = map(int,input().split())
c,d = map(int,input().split())

x = a*3+b
y = c*3+d
if x == y:
    print("NO SCORE")
elif x>y:
    print(1, x-y)
else:
    print(2, y-x)