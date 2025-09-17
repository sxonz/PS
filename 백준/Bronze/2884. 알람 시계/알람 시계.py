a,b = map(int,input().split())

sum = (a*60)+b
c = sum - 45
if(c < 0):
    t = 23
    m = 60+c
    print(t,m)
else:
    print(*divmod(c,60))