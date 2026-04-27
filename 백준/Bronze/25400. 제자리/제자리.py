n = int(input())
d = list(map(int,input().split()))
cur = 0
for i in d:
    if i == cur+1:
        cur = i
print(n-cur)
    