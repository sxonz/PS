n = int(input())
d = list(map(int,input().split()))
d.sort()
if n == 1:
    print(d[0])
    exit()

print(d[n-2])
for i in range(1,n,2):
    print(d[i-1],d[i],d[i+1])
    d[i+1] = d[i]
