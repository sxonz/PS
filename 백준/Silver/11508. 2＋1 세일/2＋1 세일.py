n = int(input())
d = [int(input()) for i in range(n)]
d.sort()
r = sum(d)
for i in range(n-3,-1,-3):
    r -= d[i]
print(r)