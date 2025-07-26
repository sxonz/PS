I,P=input,print
for _ in range(int(I())):
 n=I();P(*[n.find(str((o:=sum(map(int,n))%3)+(o==2)*3))+1,3]if"1"in n and("5"in n or len(n)<4)else[0,5]if"1"not in n else[len(n)%2,11])