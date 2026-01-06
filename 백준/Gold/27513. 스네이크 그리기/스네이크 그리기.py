n,m = map(int,input().split())
ans = []
for i in range(1,m+1):
    ans.append((1,i))
x,y = 1,n
if n%2:
    for i in range(2,n-1):
        for j in list(range(2,m+1))[::i%2*2-1]:
            ans.append((i,j))
    ans.append((n-1,m))
    cur = m-1
    if m%2:
        ans.append((n-1,m-1))
        ans.append((n,m-1))
        cur -= 1
    else:
        ans.append((n,m))
    for i in range(cur,1,-1):
        ans.append((n-i%2^1,i))
        ans.append((n-i%2,i))
    for i in range(n,1,-1):
        ans.append((i,1))
else:
    for i in range(2,n+1):
        for j in list(range(2,m+1))[::i%2*2-1]:
            ans.append((i,j))
    for i in range(n,1,-1):
        ans.append((i,1))
print(len(ans))
for i in ans:
    print(*i)
    