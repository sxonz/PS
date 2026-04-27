def gcd(a,b):return b if a%b == 0 else gcd(b,a%b)
n,m = map(int,input().split())
print(m-gcd(n,m))
