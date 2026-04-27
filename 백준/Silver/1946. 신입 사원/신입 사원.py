import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    d = [tuple(map(int,input().split())) for _ in range(n)]
    d.sort()
    minnum = int(1e9)
    ans = n
    for i,j in d:
        if minnum and j > minnum:
            ans -= 1
        minnum = min(minnum,j)
    print(ans)