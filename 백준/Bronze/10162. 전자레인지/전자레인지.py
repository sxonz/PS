t,d=int(input()),[0,0,0,300,60,10]
for i in range(3):
 while t>=d[i+3]:
  t-=d[i+3];d[i]+=1
r=[-1] if t else d
print(*r[:3])




