def dfs(s,e,m,depth,k):
    if k < 2**(depth-1):
        if depth == 2 and k == 1:
            print(s,m)
            return
        dfs(s,m,e,depth-1,k)
    elif k > 2**(depth-1):
        if depth == 2 and k == 3:
            print(m,e)
            return
        dfs(m,e,s,depth-1,k-(2**(depth-1)-1)-1)
    else:
        print(s,e)
        return

n,k = map(int,input().split())

dfs(1,3,2,n,k)