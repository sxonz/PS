n,m,k = map(int,input().split())
d = [sorted(list(map(int,input().split()))) for i in range(n)]
flag = False
for i in range(1,n):
    for j in range(m):
        if d[i-1][j] >= d[i][j]+k:
            flag = True
print("YNEOS"[flag::2])