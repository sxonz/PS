import sys
input = sys.stdin.readline
l = int(input())
cards = list(map(lambda x: x % 2,list(map(int,input().split()))))
cards2 = cards[::-1]
cnt = 0
cnt2 = 0
fcnt = 0
fcnt2 = 0
for i in cards:
    if i != 0:
        fcnt += 1
    if i == 0:
        cnt += fcnt
for i in cards2:
    if i != 0:
        fcnt2 += 1
    if i == 0:
        cnt2 += fcnt2
print(min(cnt,cnt2))