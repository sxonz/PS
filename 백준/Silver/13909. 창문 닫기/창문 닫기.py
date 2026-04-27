n = int(input())
ans = 1
while ans**2 <= n:
    ans += 1
print(ans-1)