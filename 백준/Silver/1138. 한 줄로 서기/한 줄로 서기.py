n = int(input())
d = list(map(int,input().split()))
ans = [0]*n
for v,i in enumerate(d):
    for j in range(n):
        if not i and not ans[j]:
            ans[j] = v+1
            break
        if not ans[j]:
            i -= 1
print(*ans)