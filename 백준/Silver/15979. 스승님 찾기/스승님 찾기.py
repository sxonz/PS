def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)
n,m = map(abs,map(int,input().split()))
print(2-(gcd(max(n,m),min(n,m))==1)-2*((n,m)==(0,0)))
