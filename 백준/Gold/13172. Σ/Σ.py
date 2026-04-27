import sys
input = sys.stdin.readline

MOD = 1000000007

def gcd(a,b):
    return b if a%b == 0 else gcd(b,a%b)

res = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    g = gcd(a,b)
    a //= g
    b //= g
    res += b*int(pow(a,MOD-2,MOD))
print(res%MOD)