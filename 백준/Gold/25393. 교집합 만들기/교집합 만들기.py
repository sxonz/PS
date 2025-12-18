import sys
input = sys.stdin.readline

n = int(input())
start = {}
end = {}

s = set()
for i in range(n):
    a,b = map(int,input().split())
    s.add((a,b))
    if a not in start:
        start[a] = 0
    start[a] = max(start[a],b)
    if b not in end:
        end[b] = int(1e9)
    end[b] = min(end[b],a)

for q in range(int(input())):
    a,b = map(int,input().split())
    if (a,b) in s:
        print(1)
        continue
    if a == b and a in end and b in start:
        print(2)
    elif a in start and start[a] >= b and b in end and end[b] <= a:
        print(2)
    else:
        print(-1)
