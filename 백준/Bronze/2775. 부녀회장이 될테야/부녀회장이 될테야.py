t = int(input())
k = []
n = []

for test in range(t):
    k.append(int(input()))
    n.append(int(input()))

d = [[0]*(max(n)+1) for _ in range(max(k)+1)]
for i in range(len(d[0])):
    d[0][i] = i


for i in range(1,max(k)+1):
    for j in range(1,max(n)+1):
        d[i][j] = d[i][j-1] + d[i-1][j]

for i,j in zip(k,n):
    print(d[i][j])