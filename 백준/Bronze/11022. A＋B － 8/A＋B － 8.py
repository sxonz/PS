res = []
for i in range(int(input())):
    a,b = map(int,input().split())
    res.append('Case #{0}: {1} + {2} = {3}'.format(i+1,a,b,a+b))
for i in res:
    print(i)