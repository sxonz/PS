import sys
input = sys.stdin.readline
n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
for i in range(n):
    d[i] = (d[i][0]-d[i][1],d[i][0]+d[i][1])
d.sort(key = lambda x:(x[0],-x[1]))
dp = []
stack = []
cnt = n+1
for p in d:
    s,e = p
    while stack and stack[-1][1] <= s:
        stack.pop()
    if stack and stack[-1][2] == s:
        stack[-1][2] = e
        if stack[-1][2] == stack[-1][1]:
            cnt += 1
    stack.append([s,e,s])
print(cnt)
