from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
d = [int(input()) for _ in range(n)]

p = []
m = []
one = 0
zero = 0

for i in d:
    if i > 1:
        p.append(-i)
    elif i < 0:
        m.append(i)
    elif i == 1:
        one += 1
    else:
        zero += 1

heapify(p)
heapify(m)

res = 0

while len(p) >= 2:
    a = heappop(p)
    b = heappop(p)
    res += a*b

if p:
    res -= p[0]

while len(m) >= 2:
    a = heappop(m)
    b = heappop(m)
    res += a*b

if m:
    if zero >= 1:
        zero -= 1
    else:
        res += m[0]
res += one
print(res)