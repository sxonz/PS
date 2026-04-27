d = list(map(int,input().split()))
print(max(max(d[:-1])+1,d[-1]))