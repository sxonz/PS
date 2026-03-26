d = [input().split() for i in range(10)]
for i in range(10):
    a = set()
    for j in range(10):
        a.add(d[i][j])
    if len(a) == 1:
        print(1)
        exit()

for j in range(10):
    a = set()
    for i in range(10):
        a.add(d[i][j])
    if len(a) == 1:
        print(1)
        exit()
        
print(0)