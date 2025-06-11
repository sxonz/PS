n = int(input())
d = [0]*(n+1)
d[1] = 1
color = 1
for i in range(2,n+1):
    if not d[i]:
        d[i] = (color:=color+1)
        k = 2
        while i*k <= n:
            d[i*k] = color
            k += 1
print(color)
print(*d[1:])