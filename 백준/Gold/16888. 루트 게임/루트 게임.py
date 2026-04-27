import sys
input = sys.stdin.readline
M = 1000001

win = dict()
for i in range(M):
    if i not in win:
        win[i] = False
        t = 1
        while i + t*t < M:
            win[i+t*t] = True
            t += 1
who = {True:'koosaga',False:'cubelover'}
for i in range(int(input())):
    print(who[win[int(input())]])