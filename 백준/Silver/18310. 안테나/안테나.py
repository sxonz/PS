n = int(input())
d = list(map(int,input().split()))
print(sorted(d)[(n-1)//2])
