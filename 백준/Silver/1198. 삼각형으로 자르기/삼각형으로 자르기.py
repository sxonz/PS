from itertools import combinations
import math
def ccw(a,b,c):
    return (b[0]-a[0])*(c[1]-b[1]) - (c[0]-b[0])*(b[1]-a[1])

ans = -1
d = []
for _ in range (int(input())):
    d.append(list(map(int,input().split())))

for t in combinations(d,3):
    a,b,c = t
    ans = max(ans, max(ccw(a,b,c),ccw(a,c,b))/2)
print(ans)