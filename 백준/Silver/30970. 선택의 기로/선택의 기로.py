n = int(input())
d,d2 = [],[]
for i in range(n):
    a,b = map(int,input().split())
    d.append([a,-b])
    d2.append([b,-a])
d.sort(reverse=True)
d2.sort()
print(d[0][0],-d[0][1],d[1][0],-d[1][1])
print(-d2[0][1],d2[0][0],-d2[1][1],d2[1][0])
