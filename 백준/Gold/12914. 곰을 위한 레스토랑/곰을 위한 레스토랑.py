from bisect import *

n,k = map(int,input().split())
d = list(map(int,input().split()))
ans = []
cur = []
for i in d:
    if not ans:
        ans.append(i)
        cur.append(i)
    elif i < cur[0] and i+k <= cur[0]:
        ans.append(i)
        cur.insert(0,i)
    else:
        bef = cur[0]
        i = max(i,bef+k)
        for j in cur[1:]:
            if bef <= i <= j and i+k <= j:
                ans.append(i)
                insort_left(cur,i)
                break
            bef = j
            i = max(i,j+k)
        else:
            ans.append(max(cur[-1]+k,i))
            insort_left(cur,max(cur[-1]+k,i))
print(*ans)