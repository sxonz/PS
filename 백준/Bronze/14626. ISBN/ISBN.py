c = 3
s = input()
r = sum([int(i)*c for i in s if i.isdigit()+(c:=c^2)*0])%10
print([i for i in range(10) if (i*(1+2*(s.index('*')%2))+r)%10==0][0])