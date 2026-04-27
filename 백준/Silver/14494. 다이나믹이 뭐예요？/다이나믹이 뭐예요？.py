import sys
sys.setrecursionlimit(10000)
a,b = map(int,input().split())
cache = [[0]*(b+1) for i in range(a+1)]
def what(n,m):
    if n == 1 or m == 1:
        return 1
    if cache[n][m]:
        return cache[n][m]
    cache[n][m] = (what(n-1,m-1) + what(n,m-1) + what(n-1,m)) % 1000000007
    return cache[n][m]
print(what(a,b))