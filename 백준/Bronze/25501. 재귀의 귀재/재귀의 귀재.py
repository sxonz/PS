for t in range(int(input())):
    s = input()
    l,r = 0,len(s)-1
    cnt = 0
    flag = 1
    while True:
        cnt += 1
        if l>=r:
            break
        if s[l]!= s[r]:
            flag = 0
            break
        l += 1
        r -= 1
    print(flag,cnt)