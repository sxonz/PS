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

R = [0]*n
for i in range(n):
    for l in range(log-1,-1,-1):
        if i+(1<<l) < n:
            R[i] = l
            break
cur = 0
ans = 1
for i in s:
    if i == t[cur]:
        cur += 1
        if cur >= n:
            cur = 0
            ans += 1
    else:
        i = ord(i)-97
        flag = True
        if not exist[cur][i]:
            cur = 0
            ans += 1
            if t[cur] == chr(i+97):
                cur += 1
                flag = False
                if cur >= n:
                    cur = 0
                    ans += 1
                    continue
        if flag:
            for l in range(R[cur],-1,-1):
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