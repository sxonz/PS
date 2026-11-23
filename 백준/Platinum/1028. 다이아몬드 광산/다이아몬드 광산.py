class list(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            raise IndexError
        return super().__getitem__(index)
n,m = map(int,input().split())
d = [list(map(int,input()))+[0] for i in range(n)]
d.append([0]*(m+1))
ru = [[0]*m for i in range(n)]
rd = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if d[i][j]:
            rd[i][j] += 1
            if d[i+1][j+1]:
                rd[i+1][j+1] = rd[i][j]
for i in range(n-1,-1,-1):
    for j in range(m):
        if d[i][j]:
            ru[i][j] += 1
            if d[i-1][j+1]:
                ru[i-1][j+1] = ru[i][j]

r = [[min(rd[i][j],ru[i][j]) for j in range(m)] for i in range(n)]
for i in d:
    i.pop()
    i.reverse()
    i.append(0)
    
lu = [[0]*m for i in range(n)]
ld = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if d[i][j]:
            ld[i][j] += 1
            if d[i+1][j+1]:
                ld[i+1][j+1] = ld[i][j]
for i in range(n-1,-1,-1):
    for j in range(m):
        if d[i][j]:
            lu[i][j] += 1
            if d[i-1][j+1]:
                lu[i-1][j+1] = lu[i][j]

l = [[min(ld[i][j],lu[i][j]) for j in range(m)] for i in range(n)]
for i in l:
    i.reverse()


ans = 0
for i in range(n):
    for j in range(m):
        if l[i][j]:
            try:
                for k in range(j,j+2*(l[i][j]-1)+1,2):
                    if r[i][k] >= (k-j+2)//2:
                        ans = max(ans,(k-j+2)//2)
            except:
                pass
        if r[i][j]:
            try:
                for k in range(j,j-2*(r[i][j]-1)-1,-2):
                    if l[i][k] >= (j-k+2)//2:
                        ans = max(ans,(j-k+2)//2)
            except:
                pass
print(ans)