def dfs(s,e,m,depth):
    if depth == 1:
        print(s,e)
    else: 
        dfs(s,m,e,depth-1)
        print(s,e)
        dfs(m,e,s,depth-1)

n = int(input())
print(2**n - 1)  

if n < 21:
    dfs(1,3,2,n)