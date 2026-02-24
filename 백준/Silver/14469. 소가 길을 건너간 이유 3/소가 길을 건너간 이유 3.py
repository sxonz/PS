import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
d.sort()
cur = 0
for a,b in d:
    cur = max(cur,a)+b
print(cur)
    