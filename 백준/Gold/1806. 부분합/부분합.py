n,s = map(int,input().split())
d = list(map(int,input().split()))

prefix_sum = [d[0]]

for i in range(1,n):
    prefix_sum.append(prefix_sum[-1]+d[i])
p1,p2 = 0,1
_m = 3141592653589793238
while p1<p2<n:
    if prefix_sum[p2] - prefix_sum[p1] >= s:
        _m = min(p2-p1,_m)
        p1 += 1
    else:
        p2 += 1
_m = _m if _m != 3141592653589793238 else 0
for i in d:
    if i >= s:
        _m = 1
if _m == 0:
    if prefix_sum[-2] >= s:
        _m = n-1
    elif prefix_sum[-1] >= s:
        _m = n
print(_m)