R,I=range,input
n,m = map(int,I().split())
e,t,p=[],0,list(R(n+1))
for _ in R(m):a,b,c = map(int,I().split());e+=[(c,a,b)];t += c
def U(a,b):
 a,b=F(a),F(b)
 m=min(a,b)
 p[a],p[b]=m,m
def F(x):
 if x==p[x]:return x
 p[x]=F(p[x]);return p[x]
for c,a,b in sorted(e):
 if F(a)!=F(b):U(a,b);t-=c
for i in R(n+1):F(i)
r=t if len(set(p[1:]))==1 else-1
print(r)