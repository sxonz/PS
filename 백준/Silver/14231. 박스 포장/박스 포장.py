n = int(input())
d = list(map(int,input().split()))

lis = [0]*n
for i in range(n):
    m = 0
    for j in range(i):
        if d[i]>d[j]:
            m = max(m,lis[j])
    lis[i] = m+1
print(max(lis))   
    