k,a,b = map(int,input().split())
a,b = max(a,b),min(a,b)

cur = k//a + bool(k%a)
tmp = cur*a
ans = tmp
def gcd(a,b):
    return gcd(b,a%b) if b else a
for i in range(min(b//gcd(a,b),cur)):
    tmp -= a
    if tmp < k:
        tmp += ((k-tmp)//b + bool((k-tmp)%b))*b
    ans = min(tmp,ans)

print(ans)