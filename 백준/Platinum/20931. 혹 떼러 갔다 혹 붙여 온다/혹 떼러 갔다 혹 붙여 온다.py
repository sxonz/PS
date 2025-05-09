import sys
input = sys.stdin.readline
log = 19
Q = int(input())
parents = [[0]*log]
distance = [[int(2e22)]*log]
m = 1
def adhoc(k,l):
    global m
    x = (k+last) % m
    tmp = [x]
    dtmp = [l]
    for r in range(1,log):
        tmp.append(parents[tmp[-1]][r-1])
        dtmp.append(dtmp[-1] + distance[tmp[r-1]][r-1])
    parents.append(tmp)
    distance.append(dtmp)
    m += 1
def query(x,l):
    global last
    for k in range(log-1,-1,-1):
        if l >= distance[x][k]:
            l -= distance[x][k]
            x = parents[x][k]
    last = x
    print(x)
last = 0
for q in range(Q):
    s = input().split()
    if s[0] == "query":
        query(int(s[1]),int(s[2]))
    else:
        adhoc(int(s[1]),int(s[2]))