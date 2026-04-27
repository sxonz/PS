n,a,b,c,d,e,f,g,h = map(int,input().split())
ans = []
for i in range(n+1):
    for j in range(n-i+1):
        k = n-i-j
        if i*a + j*b + k*c == d and i*e + j*f + k*g == h:
            ans.append((i,j,k))
if not ans:
    print(2)
elif len(ans) > 1:
    print(1)
else:
    print(0)
    print(*ans[0])