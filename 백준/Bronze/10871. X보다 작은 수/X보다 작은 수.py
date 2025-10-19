n,x = map(int,input().split())
d = list(map(int,input().split()))
print(*[i for i in d if i < x])