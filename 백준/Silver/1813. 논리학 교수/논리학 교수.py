n = int(input())
d = list(map(int,input().split()))
m = 0
for i in range(1,51):
    if d.count(i) == i:
        m = i
if m == 0 and 0 in d:
    m = -1
print(m)