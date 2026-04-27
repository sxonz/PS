n,k = map(int,input().split())
d = list(map(int,input().split()))
r = [d[i]-d[i-1] for i in range(1,n)]
r.sort()
print(sum(r[:-k+1] if k-1 else r))