n,q = map(int,input().split())
d = list(map(int,input().split()))
dif = []
for i in range(n-1):
    dif.append(abs(d[i+1]-d[i]))
psum = [0]
for i in dif:
    psum.append(psum[-1]+i)
for i in range(q):
    a,b = map(int,input().split())
    print(psum[b-1]-psum[a-1])