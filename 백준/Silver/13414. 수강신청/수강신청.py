k,l = map(int,input().split())
idx = dict()
for i in range(l):
    n = input()
    idx[n] = i

d = []
for i in idx:
    d.append((idx[i],i))    
d.sort()
for i in range(min(k,len(d))):
    print(d[i][1])