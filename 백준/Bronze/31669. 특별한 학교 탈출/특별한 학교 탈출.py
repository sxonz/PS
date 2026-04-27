z=input
n,m=map(int,z().split())
d=[]
for i in range(n):d.append(z())
d=list(map(list,zip(*d)))
for i in range(len(d)):
 if d[i].count('O') == 0:
  print(i+1);break
else:print('ESCAPE FAILED')