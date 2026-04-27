d = [1,1]
n = int(input())
for i in range(n):
    d.append(d[-1]+d[-2])
print(d[n-1]*2+d[n]*2)