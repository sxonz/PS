n = int(input())
d = [int(input()) for i in range(n)]
s = set(d)
a = [i for i in range(1,n+1) if i not in s]
s = set(range(n+1,500001))
b = []
for i in d:
    if i not in s:
        s.add(i)
    else:
        b.append(i)
a.sort()
b.sort()
print(sum([abs(i-j) for i,j in zip(a,b)]))
