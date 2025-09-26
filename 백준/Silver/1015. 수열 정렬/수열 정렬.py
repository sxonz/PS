n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

p = []
for i in range(n):
    p.append(b.index(a[i]))
    b[b.index(a[i])] = -1
    
print(*p)