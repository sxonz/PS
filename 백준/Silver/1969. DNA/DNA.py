n,m = map(int,input().split())

dna = [input() for i in range(n)]
d = [{"A":0,"G":0,"C":0,"T":0} for i in range(m)]
for i in range(n):
    for j in range(m):
        d[j][dna[i][j]] += 1

ans = 0
s = ''
for i in d:
    maxv = max(i.values())
    ans += n-maxv
    for j in "ACGT":
        if i[j] == maxv:
            s += j
            break
print(s)
print(ans)