path = []
def back(depth):
    if depth == m:
        print(*path)
        return
    for i in range(1,n+1):
        path.append(i)
        back(depth+1)
        path.pop()
n,m = map(int,input().split())
back(0)
