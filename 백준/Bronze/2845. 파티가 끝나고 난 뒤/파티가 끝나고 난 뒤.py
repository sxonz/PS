n,m = map(int,input().split())
print(*[i-n*m for i in list(map(int,input().split()))])