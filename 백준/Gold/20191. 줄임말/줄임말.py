log = 17

s = input()
t = input()
if set(s)-set(t):
    print(-1)
    exit()
n = len(t)
exist = [[0]*26 for i in range(n)]
for i in range(n-2,-1,-1):
    for j in range(26):
        exist[i][j] = exist[i+1][j]
    exist[i][ord(t[i+1])-97] = 1
sparse = [[[0]*26 for i in range(log)] for j in range(n)]
idx = [[0]*log for i in range(n)]
for i in range(n-1):
    idx[i][0] = i+1
    sparse[i][0][ord(t[i+1])-97] = 1
idx[n-1][0] = n

INF = int(1e9)
for k in range(1,log):
    for i in range(n):
        if idx[i][k-1] == n:
            idx[i][k] = n
        else:
            idx[i][k] = idx[idx[i][k-1]][k-1]
        if idx[i][k] < n:
            for j in range(26):
                sparse[i][k][j] = sparse[i][k-1][j] + sparse[idx[i][k-1]][k-1][j]

cur = 0
ans = 1
stack = []
for i in s[::-1]:
    stack.append(i)
while stack:
    i = stack.pop()
    if i == t[cur]:
        cur += 1
        if cur >= n:
            cur = 0
            ans += 1
    else:
        i = ord(i)-97
        if not exist[cur][i]:
            cur = 0
            ans += 1
            stack.append(chr(i+97))
            continue
        for l in range(log-1,-1,-1):
            if idx[cur][l] >= n:
                continue
            if not sparse[cur][l][i]:
                cur += 1<<l
        cur += 2
        if cur >= n:
            cur = 0
            ans += 1
if cur == 0:
    ans -= 1
print(ans)