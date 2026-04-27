n,k = map(int,input().split())
d = list(map(int,input().split()))
r = sorted(zip(d,range(n)))
r.sort(reverse=True)
ans = [0]*n
for i in r[:k]:
    ans[i[1]] = i[1]+1
    print(i[1]+1)
for i in range(k-n):
    print(0)
print(*ans,sep='\n')