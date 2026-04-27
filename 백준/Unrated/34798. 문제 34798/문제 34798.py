a,b = map(int,input().split(":"))
c,d = map(int,input().split(":"))
if a*60+b < c*60+d:
    print("YES")
else:
    print("NO")