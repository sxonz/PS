l,n = map(int,input().split())
d = [input() for i in range(n)]
k = int(input())
s = set()
for i in range(n):
    for j in range(l-k+1):
        s.add(d[i][j:j+k])
s = list(s)
ans = 0
for i in s:
    tmp = 0
    for j in d:
        for idx in range(l-k+1):
            if j[idx:idx+k] == i:
                tmp += 1
    ans = max(ans,tmp)
print(ans) 