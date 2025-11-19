n = int(input())
k = int(input()) - 1
d = list(map(int,input().split()))
d.sort()
r = [d[i]-d[i-1] for i in range(1,n)]
r.sort()
print(sum(r[:-k] if k else r))