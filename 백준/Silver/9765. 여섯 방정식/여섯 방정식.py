def gcd(a,b):
    return a if not b else gcd(b,a%b)
c1,c2,c3,c4,c5,c6 = map(int,input().split())
x2 = gcd(c1,c5)
x6 = gcd(c3,c6)
print(c1//x2,x2,c5//x2,c6//x6,x6,c3//x6)