n = int(input())
d = [[0]*100 for i in range(100)]
for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            d[j][k] = 1
print(sum([sum(i) for i in d]))