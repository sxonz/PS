n = int(input())
d = list(map(int,input().split()))
temp = sorted(set(d))
coord = dict()
for i in range(len(temp)):
    coord[temp[i]] = i
for i in d:
    print(coord[i],end=' ')