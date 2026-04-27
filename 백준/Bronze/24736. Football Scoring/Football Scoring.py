res=[]
for _ in range(2):
    l = list(map(int,input().split()))
    res.append(sum(l)+sum(l[::2])+(l[0]*2+l[1])*2)
print(*res)