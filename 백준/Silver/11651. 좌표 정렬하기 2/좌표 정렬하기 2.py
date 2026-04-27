import sys
input = sys.stdin.readline
for i in sorted([list(map(int,input().split())) for _ in range(int(input()))],key = lambda x:(x[1],x[0])):
    print(i[0],i[1])