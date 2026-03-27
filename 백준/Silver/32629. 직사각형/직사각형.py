import sys
input = sys.stdin.readline

MAX = 100000
for t in range(int(input())):
    n = int(input())
    r = int(n**0.5)
    if r*r < n:
        r += 1
    for i in range(r,-1,-1):
        if r*i < n:
            print(r*2+i*2+2)
            break
    