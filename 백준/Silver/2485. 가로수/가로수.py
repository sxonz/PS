def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)
n = int(input())
d = [int(input()) for i in range(n)]
g = d[1]-d[0]
for i in range(2,n):
    g = gcd(g,d[i]-d[i-1])

print((d[-1]-d[0])//g-n+1)