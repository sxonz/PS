def gcd(a,b):
    return b if a%b == 0 else gcd(b,a%b)

a,b = map(int,input().split())
s = a*b
div = set()
for i in range(1,s+1):
    if s % i == 0 and i*s//i//gcd(i,s//i) == b:
        if i in div:
            break
        div.add(s//i)

if a != b:
    print(s//i,i)
else:
    print(a,b)