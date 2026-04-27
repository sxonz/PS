a,b = map(int,input().split())
k,x = map(int,input().split())
r = set(range(k-x,k+x+1))
d = [i for i in range(a,b+1) if i in r]
d = len(d) if d else "IMPOSSIBLE"
print(d)