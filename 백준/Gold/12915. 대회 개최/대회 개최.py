e,em,m,mh,h = map(int,input().split())
ans = 0
while True:
    if not e:
        if not em:
            break
        em -= 1
    else:
        e -= 1
    if not h:
        if not mh:
            break
        mh -= 1
    else:
        h -= 1
    if not m:
        if not em+mh:
            break
        if em>mh:
            em -= 1
        else:
            mh -= 1
    else:
        m -= 1
    ans += 1
print(ans)