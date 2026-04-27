import sys
input=sys.stdin.readline
n,s,p = map(int,input().split(" "))
if n == 0:
    print(1)
else:
    scores = list(map(int,input().split(" ")))
    if p == len(scores) and min(scores) >= s:
        print(-1)
    else:
        scores.append(s)
        scores.sort(reverse=True)
        temp = {}
        for i in range(len(scores)):
            if scores[i] not in temp:
                temp[scores[i]] = i+1
        print(temp[s])