n = int(input())
d = list(map(int,input().split()))
d.reverse()
r = 0
for i in d:
    k = max(r//i*i,i)
    while k < r:
        k += i
    r = k
print(r)