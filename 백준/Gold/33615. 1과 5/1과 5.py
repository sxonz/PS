I,P=input,print
for t in range(int(I())):
 n=I()
 if"1"not in n:P(0,5);continue
 if"5"not in n and(m:=len(n))>3:P(m%2,11);continue
 mod=sum(int(i) for i in n)%3;P(n.find(str(mod+(mod==2)*3))+1,3)
