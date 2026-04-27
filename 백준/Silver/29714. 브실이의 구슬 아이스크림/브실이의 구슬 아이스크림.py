from copy import deepcopy
from collections import defaultdict
ili = int(input())
l1l1i11li = defaultdict(int)
lil111lil = 1
temp = list(map(int,input().split()))
for iiiii in temp:
    l1l1i11li[iiiii] += lil111lil
    
l = int(input())
for _ in range(l):
    li1li1li1 = list(map(int,input().split()))
    l1il1il1i = list(map(int,input().split()))
    il11i1l1l = defaultdict(int)
    for i in li1li1li1[lil111lil:]:
        il11i1l1l[i] += lil111lil
    flag = 0
    for key in il11i1l1l.keys():
        if il11i1l1l[key] > l1l1i11li[key]:
            flag = lil111lil
    if not flag:
         for i in li1li1li1[lil111lil:]:
            l1l1i11li[i] -= lil111lil
         for i in l1il1il1i[lil111lil:]:
            l1l1i11li[i] += lil111lil
lllll = []
for iiiii,ll in l1l1i11li.items():
    for k in range(ll):
        lllll.append(iiiii)
print(len(lllll))
if lllll:
    print(*lllll)