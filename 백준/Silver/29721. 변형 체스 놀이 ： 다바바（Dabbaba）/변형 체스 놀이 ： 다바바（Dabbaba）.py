import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dabbaba = set()
for i in range(k):
    dabbaba.add(tuple(map(int,input().split())))

board = set()

for x,y in dabbaba:
    if 0<x+2<n+1:
        if (x+2,y) not in dabbaba:
            board.add((x+2,y))
    if 0<x-2<n+1:
        if (x-2,y) not in dabbaba:
            board.add((x-2,y))
    if 0<y+2<n+1:
        if (x,y+2) not in dabbaba:
            board.add((x,y+2))
    if 0<y-2<n+1:
        if (x,y-2) not in dabbaba:
            board.add((x,y-2))

print(len(board))