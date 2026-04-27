a,b = map(int,input().split())
a,b = min(a,b),max(a,b)
if b-a > 1:
    print(b-a-1)
    print(*[i for i in range(a+1,b)])
else:
    print(0)