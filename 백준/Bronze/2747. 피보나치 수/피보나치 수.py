n = int(input())
d = [1,1]
for i in range(n-2):
    d.append(d[-1]+d[-2])
print(d[n-1])
