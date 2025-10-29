input()
a = list(map(int,input().split()))
input()
b = list(map(int,input().split()))

res = []
while a and b:
    r = a.index(max(a))
    if a[r] in b:
        res.append(a[r])
        b = b[b.index(a[r])+1:]
        a = a[r+1:]
    else:
        a.pop(r)
print(len(res))
print(*res)