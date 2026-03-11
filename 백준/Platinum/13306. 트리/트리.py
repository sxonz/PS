import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)

n,q = map(int,input().split())
tmp = [0,0]+[int(input()) for i in range(n-1)]
par = list(range(n+1))
def F(x):
    if x != par[x]:
        par[x] = F(par[x])
    return par[x]
def U(a,b):
    a,b = F(a),F(b)
    if a<b:
        par[b] = a
    else:
        par[a] = b

query = [tuple(map(int,input().split())) for i in range(n-1+q)][::-1]
ans = []
for Q in query:
    q,*r = Q
    if q == 0:
        U(r[0],tmp[r[0]])
    else:
        if F(r[0]) == F(r[1]):
            ans.append("YES")
        else:
            ans.append("NO")
print(*ans[::-1],sep='\n')