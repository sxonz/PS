def check(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:return False
    return True
def dfs(n,k):
    if k == l:
        if check(n):
            print(n)
        return
    n *= 10
    for i in range(10):
        if check(n+i):
            dfs(n+i,k+1)
l=int(input())
for i in (2,3,5,7):
    dfs(i,1)