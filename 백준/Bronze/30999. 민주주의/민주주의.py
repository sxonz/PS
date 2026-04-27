n,m = map(int,input().split())
ans = 0
for i in range(n):
    s = input()
    if s.count("O") > m//2:
        ans += 1
print(ans)