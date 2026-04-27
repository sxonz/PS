n = int(input())
d = list(map(int,input().split()))
m = set()
for i in range(n-1,-1,-1):
    for j in range(i):
        if d[i] != d[j]:
            m.add(abs(d[i] - d[j]))
m = list(m)
def gcd(a,b):return b if a%b == 0 else gcd(b,a%b)
if len(m) == 1:
    print(m[0])
else:
    g = gcd(m[0],m[1])
    for i in range(2,len(m)):
        g = gcd(g,m[i])
    print(g)