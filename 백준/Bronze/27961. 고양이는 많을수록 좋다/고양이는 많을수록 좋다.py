n = int(input())
ans = 1
cur = 1
for i in range(n):
    if cur >= n:
        print(i+1)
        break
    cur *= 2
else:
    print(0)