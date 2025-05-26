n = int(input())
to = list(map(int,input().split()))
d = list(map(int,input().split()))
res = [0]*n
for k in range(3):
    for i in range(n):
        res[i] = d[to[i]-1]
    d,res = res[::],[0]*n

for i in d:
    print(i)