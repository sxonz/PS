def v(x,y,s):
    dis = (x**2+y**2)**0.5
    return dis/s
    
n = int(input())
d = []
for i in range(n):
    tmp = list(map(int,input().split()))
    d.append((v(tmp[0],tmp[1],tmp[2]),i+1))
d.sort()
for i in d:
    print(i[1])