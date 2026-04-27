n = int(input())
p = list(map(int,input().split()))
d = [[],[],[],[],[],[]]
for i in range(n):
    a,b = map(int,input().split())
    d[a].append(b)
for i in range(5):
    d[i+1] = sorted(d[i+1])[:p[i]]
print(240 + sum([sum(i)-i[0]+i[-1] for i in d[1:]]))