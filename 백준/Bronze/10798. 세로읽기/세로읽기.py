a = [list(input()) for _ in range(5)]
ans = ''
while a != [[],[],[],[],[]]:
    for i in range(5):
        if a[i]:ans += a[i].pop(0)
print(ans)