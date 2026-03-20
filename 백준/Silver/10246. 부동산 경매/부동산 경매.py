import sys
input = sys.stdin.readline

MAX = 1000001
d = [1]*MAX
d[1] = 0
w = 1
for i in range(2,1500):
    for j in range(2,MAX//i):
        if i*j+w >= MAX:
            break
        d[i*j+w] += 1
    w += i
while True:
    n = int(input())
    if not n:
        break
    print(d[n])