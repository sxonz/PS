n,r,c = map(int,input().split())
n = 2**n
s = n//2
answer = 0
while True:
    if c >= s:
        answer += s**2
        c -= s
    if r >= s:
        answer += s**2 * 2
        r -= s
    if s == 1:
        break
    s //= 2
print(answer)