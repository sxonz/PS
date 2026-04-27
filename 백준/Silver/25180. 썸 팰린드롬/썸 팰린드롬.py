n = int(input())
ans = n//18*2
n %= 18
if n:
    if n<10:
        ans += 1
    else:
        ans += 2+n%2
print(ans)