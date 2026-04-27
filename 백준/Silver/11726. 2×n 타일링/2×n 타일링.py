n = int(input())

d = [1,1]

for i in range(n-1):
    d.append(d[-1] + d[-2])
print(d[n] % 10007)