I=lambda:map(int,input().split())
n,m,t=I()
e=[list(I())for _ in range(m)]
e.sort(key=lambda x:x[2])
p=list(range(n+1))
def find(x):
 if x-p[x]:p[x]=find(p[x])
 return p[x]
tmp=cost=0
for a,b,c in e:
 a,b=find(a),find(b)
 if a-b:p[max(a,b)]=min(a,b);cost+=c+tmp;tmp+=t
print(cost)
