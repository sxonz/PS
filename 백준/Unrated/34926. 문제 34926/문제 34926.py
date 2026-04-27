n,k = map(int,input().split())
s = input()
d = [0]*n
d[0] = 1
for i in range(n):
    if not d[i]:
        continue
    for nx in i+1,i+k:
        if nx>=n:
            break
        if s[nx] == "_":
            d[nx] = 1

if d[-1]:
    print("YES")
else:
    print("NO")