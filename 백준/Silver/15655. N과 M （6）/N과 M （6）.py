n,m = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
path = []
def back(idx,cur):
    if cur == m:
        print(*path)
        return
    for i in range(idx,n):
        path.append(d[i])
        back(i+1,cur+1)
        path.pop()
back(0,0)
