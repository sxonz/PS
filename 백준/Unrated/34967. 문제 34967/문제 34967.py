n = int(input())

def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)
s,e = 1,19998
ans = [1]
l = 1
while l < n:
    ans.append(s*e)
    s += 1
    ans.append(s*e)
    e -= 1
    l += 2
ans = ans[:n]
if n == 20000:
    ans.pop()
    ans.append(20000)
print(*ans[:n])
