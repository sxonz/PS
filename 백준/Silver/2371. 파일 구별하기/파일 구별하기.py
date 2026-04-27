import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int,input().split()[:-1])) for i in range(n)]
tmp = max([len(i) for i in d])

for i in range(n):
    for j in range(tmp-len(d[i])):
        d[i].append(0)

s = ['' for i in range(n)]
for k in range(tmp):
    for i in range(n):
        s[i] += str(d[i][k])
    if len(set(s)) == n:
        print(k+1)
        break