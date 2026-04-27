n = int(input())
d = [(i,j) for i,j in zip(list(map(int,input().split())), list(map(int,input().split())))]
d.sort()
s = sum(i[1] for i in d)
ans = 0
for i in d:
    ans = max(ans,i[0]*s)
    s -= i[1]
print(ans)