n = int(input())
d = list(map(int,input().split()))
res = 0
for i in range(n):
    a,b = map(int,input().split())
    if d[i] and b>a:
        res += b-a
print(res)