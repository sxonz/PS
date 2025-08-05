n,m,k = map(int,input().split())
d = []
for i in range(n):
    a = list(input())
    a.sort()
    d.append(''.join(a))
d = ''.join(sorted(d)[:k])
print(''.join(sorted(d)))
