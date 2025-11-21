for t in range(int(input())):
    n = input()
    s,e = 0,len(n)-1
    ans = 0
    while s < e:
        if n[s] != n[e]:
            if n[s+1:e+1] == n[s+1:e+1][::-1] or n[s:e] == n[s:e][::-1]:
                ans = 1
            else:
                ans = 2
            break
        else:
            s += 1
            e -= 1
    print(ans)