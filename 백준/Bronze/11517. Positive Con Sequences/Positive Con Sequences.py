import sys
for l in sys.stdin:
 l=l.strip()
 if not l:continue
 p=l.split()
 if len(p)!=4:continue
 a,b,c,d=map(int,p)
 if a==b==c==d==-1:break
 x=[a,b,c,d]
 m=x.index(-1)
 def f(a,b,c,d,m):
  if m==0:
   r=c-b; x=b-r; return x if d-c==r and 1<=x<=10000 and x<=b else None
  if m==1:
   r=(d-a)//3 if (d-a)%3==0 else None; 
   if r is None:return None
   x=a+r; return x if a+2*r==c and 1<=x<=10000 and a<=x<=c else None
  if m==2:
   r=b-a; x=b+r; return x if d==b+2*r and 1<=x<=10000 and b<=x<=d else None
  if m==3:
   r=b-a; x=a+3*r; return x if c==a+2*r and 1<=x<=10000 and c<=x else None
 def g(a,b,c,d,m):
  if m==0:
   if b==0:return None
   r=c//b if c%b==0 else None
   if r is None or r==0:return None
   x=b//r if b%r==0 else None
   return x if x is not None and d==c*r and 1<=x<=10000 and x<=b else None
  if m==1:
   if a==0 or d%a!=0:return None
   v=d//a; r=int(round(v**(1/3)))
   if r**3!=v:return None
   x=a*r; return x if c==a*r*r and 1<=x<=10000 and a<=x<=c else None
  if m==2:
   if a==0 or b%a!=0:return None
   r=b//a; x=a*r*r; return x if d==a*r*r*r and 1<=x<=10000 and b<=x<=d else None
  if m==3:
   if a==0 or b%a!=0:return None
   r=b//a; x=a*r*r*r; return x if c==a*r*r and 1<=x<=10000 and c<=x else None
 y=f(a,b,c,d,m); z=g(a,b,c,d,m)
 print(y if y is not None else z if z is not None else -1)
