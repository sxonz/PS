import sys
input = sys.stdin.readline

for t in range(int(input())):
    x,y = map(int,input().split())
    if x <= 2:
        tmp = 1
    else:
        tmp = x//2+1
    if tmp > y:
        tmp = y
    print(x,tmp)