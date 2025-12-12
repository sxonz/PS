import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = list(map(int,input().split()))
dif = [0]*(n+1)
for i in range(m):
    a,b,k = map(int,input().split())
    dif[a-1] += k
    dif[b] -= k

psum = [0]
for i in dif:
    psum.append(psum[-1]+i)

for i,j in zip(d,psum[1:]):
    print(i+j,end=' ')