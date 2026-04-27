n = int(input())
d = [input() for i in range(n)]
d2 = list(zip(*d))
d2 = [''.join(i) for i in d2]
c1,c2 = 0,0
for i in d:
    c1 += sum([1 for j in i.split("X") if len(j) >= 2])
for i in d2:
    c2 += sum([1 for j in i.split("X") if len(j) >= 2])
print(c1,c2)