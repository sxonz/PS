from collections import deque
import sys
input = sys.stdin.readline

test = int(input())
for i in range(test):
    query = input()
    n = int(input())
    d = deque(input().lstrip('[').rstrip(']\n').split(','))
    if n == 0:
        if 'D' in query:
            print('error')
            continue
        else:
            print('[]')
            continue
    rev = 0
    d2 = deque(reversed(d))
    flag = False
    for i in query:
        if i == 'R':
            rev ^= 1
        elif i == 'D':
            if rev:
                if d:
                    d.pop()
                    d2.popleft()
                else:
                    print('error')
                    flag = True
                    break
            else:
                if d:
                    d.popleft()
                    d2.pop()
                else:
                    print('error')
                    flag = True
                    break
    if flag:
        continue
    if rev:
        print('['+','.join(d2)+']')
    else:
        print('['+','.join(d)+']')