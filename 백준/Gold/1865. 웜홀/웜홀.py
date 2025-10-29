for test in range(int(input())):
    n,m,w = map(int,input().split())
    edges = []
    for i in range(m):
        a,b,c = map(int,input().split())
        edges.append((a,b,c))
        edges.append((b,a,c))
    for i in range(w):
        a,b,c = map(int,input().split())
        edges.append((a,b,-c))
    
    visited = [False]*(n+1)
    def bel(x):
        distance = [int(1e10)]*(n+1)
        distance[x] = 0
        for v in range(n):
            for s,e,cost in edges:
                if distance[s] != int(1e10) and distance[s]+cost < distance[e]:
                    if v == n-1:
                        return True
                    else:
                        visited[e] = True
                        distance[e] = distance[s] + cost
        return False
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            if bel(i):
                print("YES")
                break
    else:
        print("NO")