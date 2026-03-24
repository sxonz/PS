s = input()
n = int(input())
ans = 0
for i in range(n):
    t = input()*2
    if s in t:
        ans += 1
print(ans)