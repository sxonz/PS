n = int(input())
res = 0
for i in range(n):
    a,b,c,d = map(int,input().split())
    res += a>=1000 or b >= 1600 or c >= 1500 or (d >0 and d <= 30)
print(res)
        