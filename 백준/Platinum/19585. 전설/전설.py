import sys
input = lambda:sys.stdin.readline().strip()

n,m = map(int,input().split())
color = [input() for i in range(n)]
nick = set([input() for i in range(m)])

d = dict()

for i in color:
    cur = d
    for j in i:
        if j not in cur:
            cur[j] = dict()
        cur = cur[j]
    cur[''] = ''

for i in range(int(input())):
    team = input()
    cur = d
    flag = False
    for k in range(len(team)):
        if '' in cur:
            if team[k:] in nick:
                flag = True
                break
            if team[k] not in cur:
                if team[k:] in nick and k:
                    flag = True
                break
        if team[k] not in cur:
            break
        cur = cur[team[k]]
    print("YNeos"[flag^1::2])