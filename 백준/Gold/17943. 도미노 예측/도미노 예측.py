import sys
input = sys.stdin.readline
n,q = map(int,input().split())
d = list(map(int,input().split()))
pxor = [0,0]
for i in d:
    pxor.append(pxor[-1]^i)

for i in range(q):
    query,*p = map(int,input().split())
    if query == 0:
        print(pxor[p[0]]^pxor[p[1]])
    else:
        print(pxor[p[0]]^pxor[p[1]]^p[2])