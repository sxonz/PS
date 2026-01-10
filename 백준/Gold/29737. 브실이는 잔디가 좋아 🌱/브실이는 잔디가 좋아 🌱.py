n,k = map(int,input().split())
d = [[0,0,0,0,''] for i in range(n)]
for p in range(n):
    handle = input()
    s = [input() for i in range(7)]
    s = list(map(list,zip(*s)))
    s = ''.join([''.join(i) for i in s])+"X"
    maxstreak = 0
    streak = 0
    start = -1
    curstart = -1
    freeze = 0
    curfreeze = 0
    tmpfreeze = 0
    fail = 0
    for i in range(k*7+1):
        cur = s[i]
        if cur == "O":
            if not streak:
                curstart = i
            streak += 1
            curfreeze += tmpfreeze
            tmpfreeze = 0
        elif cur == "F":
            if streak:
                tmpfreeze += 1
        else:
            if streak:
                if streak > maxstreak:
                    maxstreak = streak
                    freeze = curfreeze
                    start = curstart
                elif streak == maxstreak:
                    if curfreeze < freeze:
                        freeze = curfreeze
                        start = curstart
            fail += 1
            streak = 0
            curfreeze = 0
            tmpfreeze = 0
            curstart = -1
    d[p] = [-maxstreak,freeze,start,fail,handle]
d.sort()
print(1,". ",d[0][4],sep='')
ans = [1]
for i in range(1,n):
    r = ans[-1]+1
    if d[i][:4] == d[i-1][:4]:
        r = ans[-1]
    print(r,". ",d[i][4],sep='')
    ans.append(r)   