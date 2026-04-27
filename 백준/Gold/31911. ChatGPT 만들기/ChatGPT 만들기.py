A = 97
_range = [-52,-6,-4,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
n,k,l = map(int,input().split())
d = dict()

for i in _range:
    tmp = dict()
    for j in _range:
        tmp[chr(j+A)] = 0
    d[chr(i+A)] = tmp

m = 0
for i in range(n):
    s = input()
    before = '['
    for i in range(1,len(s)):
        d[before][s[i]] += 1
        before = s[i]

for i in d:
    tmp = max(d[i].values())
    for j in _range:
        if d[i][chr(j+A)] == tmp:
            d[i] = chr(j+A)
            break
    
res = '['
bef = '['
flag = True
for i in range(k+l-1):
    if flag:
        res += d[bef]
        bef = d[bef]
        if bef == ']':
            flag = False
    else:
        res += '.'

print(res[k-1:k+l-1])