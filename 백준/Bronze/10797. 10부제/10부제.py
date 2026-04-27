n = int(input())
print(sum([1 if i == n else 0 for i in list(map(int,input().split()))]))