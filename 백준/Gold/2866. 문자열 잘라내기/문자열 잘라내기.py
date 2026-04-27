r,c = map(int,input().split())
d = list(map(''.join,zip(*[input() for _ in range(r)])))
s = 1
e = r
last = 0
while s<=e:
    mid = (s+e)//2
    tmp = set()
    for i in d:
        tmp.add(i[mid:r+1])
    if len(tmp) != c:
        e = mid-1
    if len(tmp) == c:
        s = mid+1
        last = mid
print(last)