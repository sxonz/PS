a,b,c = map(int,input().split())
d = a*3+b*20+c*120
e,f,g = map(int,input().split())
h = e*3+f*20+g*120
if d>h:
    print("Max")
elif h>d:
    print("Mel")
else:
    print("Draw")