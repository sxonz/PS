n,k = map(int,input().split())
d = list(map(int,input().split()))
d.sort(reverse=True)
print(sum(d[:k])-k*(k-1)//2)