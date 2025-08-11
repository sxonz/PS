N = 10**7
p = [1]*N
for i in range(2, int(N**0.5)+1):
    if p[i]:
        for j in range(i+i, N, i):
            p[j] = 0

print([i for i in range(2,N) if p[i]][int(input())-1])