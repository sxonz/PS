from math import *

n,r,g,b = map(int,input().split())
d = [[] for i in range(n+1)]
val = dict()
for i in range(1,n+1):
    if r>=i:
        d[i].append((i,0,0))
        val[(i,0,0)] = 1
    if g>=i:
        d[i].append((0,i,0))
        val[(0,i,0)] = 1
    if b>=i:
        d[i].append((0,0,i))
        val[(0,0,i)] = 1
    if i%2==0:
        if g>=i//2 and b>=i//2:
            d[i].append((0,i//2,i//2))
            val[(0,i//2,i//2)] = comb(i,i//2)
        if r>=i//2 and b>=i//2:
            d[i].append((i//2,0,i//2))
            val[(i//2,0,i//2)] = comb(i,i//2)
        if r>=i//2 and g>=i//2:
            d[i].append((i//2,i//2,0))
            val[(i//2,i//2,0)] = comb(i,i//2)
    if i%3==0:
        d[i].append((i//3,i//3,i//3))
        val[(i//3,i//3,i//3)] = factorial(i) // factorial(i//3)**3

def back(r,g,b,depth):
    tmp = 0
    if depth == n+1:
        return 1
    for x,y,z in d[depth]:
        if r>=x and g>=y and b>=z:
            tmp += back(r-x,g-y,b-z,depth+1)*val[(x,y,z)]
    return tmp
print(back(r,g,b,1))