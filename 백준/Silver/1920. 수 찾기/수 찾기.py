n = int(input())
nums = set(list(map(int,input().split())))
m = int(input())
f = list(map(int,input().split()))
for i in f:
    print(int(i in nums))