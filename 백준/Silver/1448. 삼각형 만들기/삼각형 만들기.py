import sys
input = sys.stdin.readline
n = int(input())
m = sorted([int(input()) for _ in range(n)], reverse=True)

for i in range(n-2):
    if m[i] < m[i+1]+m[i+2]:
        print(m[i]+m[i+1]+m[i+2])
        break
else:
    print(-1)