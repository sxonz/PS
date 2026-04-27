n,m = map(int,input().split())
d = []
for i in range(n):
    d.append(list(map(int,input().split())))

d = list(map(list,zip(*d)))
a = int(input())
dp = [0,sum(d[0])]
for i in range(1,len(d)):
    dp.append(sum(d[i]) + dp[-1])
    
p1,p2 = 0,a
result = []

while p2 < len(dp):
    result.append(dp[p2]-dp[p1])
    p1 += 1;p2 += 1
print(max(result))