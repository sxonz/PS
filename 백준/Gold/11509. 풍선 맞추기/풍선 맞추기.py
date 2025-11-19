n = int(input())
d = list(map(int,input().split()))
cur = [0]*(max(d)+2)
ans = 0
for i in d:
    if cur[i+1]:
        cur[i+1] -= 1
    cur[i] += 1
print(sum(cur))