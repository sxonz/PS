n = int(input())
d = list(map(int, input().split()))
 
for i in range(n-1, 0, -1):
    if d[i-1]>d[i]:
        t = i-1
        break
else:
    print(-1)
    exit()
    
for i in range(n-1, 0,-1):
    if d[i]<d[t]:
        d[i], d[t] = d[t], d[i]
        break
d = d[:t+1] + sorted(d[t+1:], reverse=True)
print(*d)