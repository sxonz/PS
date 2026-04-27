n = int(input())
d=list(map(int,input().split()))
if sum(d) != 0:
 while d[-1]==0:d=[0]+d[:-1]
r,e=0,0
for i in d:
 if i==0:r+=1
 else:
   e+=(r+1)//2
   r=0
print(e+sum(d)+(r+1)//2)