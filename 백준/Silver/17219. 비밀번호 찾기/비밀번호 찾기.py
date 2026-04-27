import sys
I = sys.stdin.readline
n,m = map(int,I().split())
d = dict()
for i in range(n):
    r = I().split()
    d[r[0]] = r[1]
for i in range(m):
    a = input()
    print(d[a])