import sys
R,I=range,sys.stdin.readline;g=18;sys.setrecursionlimit(1<<g);L,n,S=R(g-1,-1,-1),int(I())+1,lambda:map(int,I().split());N=R(n);T,P,D,v,d=[0]*n,[[1]*(g+1) for _ in N],[[0]*(g+1) for _ in N],[0]*n,[[] for _ in N]
for _ in R(n-2):a,b,w =S();d[a]+=[(b,w)];d[b]+=[(a,w)]
v[1]=1
def F(u,w):
 for X,c in d[u]:
  if v[X]==0:v[X]=1;T[X]=w+1;P[X][0]=u;D[X][0]=c;F(X,w+1)
F(1,0)
for k in R(1,g):
 for i in R(n):P[i][k],D[i][k]=P[K:=P[i][k-1]][k-1],D[i][k-1]+D[K][k-1]
def j(a,b):
 if T[a]>T[b]:
  a,b = b,a
 for k in L:
  if T[b]-T[a]>=1<<k:b=P[b][k]
 if a == b:return a
 for i in L:
  if (A:=P[a][i])!=(B:=P[b][i]):a,b=A,B
 return P[a][0]
def C(a,b):
 c=0
 for k in L:
  if T[b]-T[a]>=1<<k:c+=1<<k;b=P[b][k]
 return c+(a!=b)
def A(V):
 s,e=V;r=0
 if T[s]>T[e]:s,e=e,s
 for k in L:
  if T[e]-T[s]>=1<<k:r+=D[e][k];e=P[e][k]
 if s==e:return r
 for k in L:
  if(X:=P[s][k])!=(Y:=P[e][k]):r+=D[s][k]+D[e][k];s,e=X,Y
 return r+D[s][0]+D[e][0]
def B(V):
 s,e,h=V;m=j(s,e);A=C(m,s);h-=1
 if A > h:
  for k in L:
   if 1<<k<=h:h-=1<<k;s=P[s][k]
  return s
 A+=C(m,e)-h
 for k in L:
  if 1<<k<=A:A-=1<<k;e=P[e][k]
 return e
for _ in R(int(I())):q,*Q=list(S());print(A(Q) if q==1 else B(Q))