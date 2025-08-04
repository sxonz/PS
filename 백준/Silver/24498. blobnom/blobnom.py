n = int(input())
d = list(map(int,input().split()))
print(max([d[i]+min(d[i-1],d[i+1]) for i in range(1,n-1)]+[d[0],d[-1]]))