n = int(input())
d = list(map(int,input().split()))
_find = int(input())

two = dict()
for i in range(10):
    two[2**i] = i

key = dict()
for i in range(8):
    key[i] = i

for i in d:
    a,b = 0,0
    for j in two:
        if i-j in two:
            a,b = j,i-j
            break
    else:
        continue
    a,b = two[a],two[b]
    key[a],key[b] = key[b],key[a]
print(key[_find])