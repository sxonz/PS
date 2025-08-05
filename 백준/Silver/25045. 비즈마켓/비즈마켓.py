n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse=True)
b.sort()
a = a[:min(n,m)]
b = b[:min(n,m)]
print(sum([max(0,i-j) for i,j in zip(a,b)]))