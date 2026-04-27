def gcd(n1,n2):return n2 if n1%n2 == 0 else gcd(n2,n1%n2)

a,b = map(int,input().split())
c,d = map(int,input().split())

n = a*d+c*b
m = b*d
print(n//gcd(n,m),m//gcd(n,m))