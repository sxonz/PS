n,m,k,x,y = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(n)]
r = []
for i in d:
    r.append(x*i[0]-y*i[1])
r.sort()
print(k*(x+y)+sum(r[:m]))