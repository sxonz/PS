n,m = map(int,input().split())
d = list(map(int,input().split()))
print("DOIUMTI"[sum([i-1 for i in d]) < m::2])