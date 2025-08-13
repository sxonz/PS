import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = dict()
for _ in range(n) :
    board[input()] = 1
    
res = n
for _ in range(m) :
    tmp = sorted(input().split(','))
    
    for t in tmp :
        if t in board.keys() :
            if board[t] == 1 :
                board[t] -= 1
                res -= 1
    print(res)
