n = int(input())
d = [n]
for i in range(n-1):
    if i%2:
        d.append(d[-1]+n-i-1)
    else:
        d.append(d[-1]-(n-i-1))
print(*d)