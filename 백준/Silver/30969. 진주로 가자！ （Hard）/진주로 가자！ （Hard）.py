import sys
input = sys.stdin.readline
n = int(input())
d = [0]*1001
j = 0
lj = 0
for i in range(n):
    a,b = input().split()
    b = int(b)
    if a == 'jinju':
        j = b
    if b > 1000:
        lj += 1
    else:
        d[b] += 1
print(j)
print(sum(d[j+1:])+lj)