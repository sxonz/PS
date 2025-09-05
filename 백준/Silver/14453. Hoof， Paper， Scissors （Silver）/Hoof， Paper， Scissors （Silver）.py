n = int(input())
p = {"H" : 0, "P" : 1, "S" : 2}
d = [p[input()] for i in range(n)]
l = [0,0,0]
r = [0,0,0]
for i in d:
    r[i] += 1

m = max(max(l),max(r))
for i in d:
    r[i] -= 1
    l[i] += 1
    m = max(m,max(l)+max(r))
print(m)