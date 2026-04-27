n = int(input())
print(sum([(n-idx)*value for idx,value in enumerate(sorted(list(map(int,input().split()))))]))