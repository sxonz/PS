d = list(map(int,input().split()))
print(*[j-i for i,j in zip(d,[1,1,2,2,2,8])])