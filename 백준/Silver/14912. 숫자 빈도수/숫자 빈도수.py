n,d = map(int,input().split())
print(sum([str(i).count(str(d)) for i in range(1,n+1)]))
    