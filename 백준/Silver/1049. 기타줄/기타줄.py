n,m = map(int,input().split())
d = [tuple(map(int,input().split())) for _ in range(m)]
six = min([i[0] for i in d])
one = min([i[1] for i in d])
osix = one*6
ans = 0
while n>6:
    ans += min(osix,six)
    n -= 6
ans += min(six,one*n)
print(ans)
