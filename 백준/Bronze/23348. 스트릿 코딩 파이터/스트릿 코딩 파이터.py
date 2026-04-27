a,b,c = map(int,input().split())
ans = 0
for i in range(int(input())):
    tmp = 0
    for j in range(3):
        x,y,z = map(int,input().split())
        tmp += x*a+y*b+z*c
    ans = max(ans,tmp)
print(ans)