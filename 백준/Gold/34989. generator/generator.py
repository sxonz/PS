n = int(input())
d = list(map(int,input().split()))
res = input()
if res == "no":
    s = [i for i in range(1,2001) if i not in d]
    idx = 0
    ans = []
    for i in d:
        if i:
            ans.append(i)
        else:
            ans.append(s[idx])
            idx += 1
    print(*ans)
else:
    for k in range(n//2):
        tmp = d[::]
        for i in range(k+1):
            l,r = d[k-i],d[-i-1]
            if not l and not r:
                tmp[k-i] = 1
                tmp[-i-1] = 1
            elif not l:
                tmp[k-i] = r
            elif not r:
                tmp[-i-1] = l
            else:
                if l != r:
                    break
        else:
            for i in range(n):
                if not tmp[i]:
                    tmp[i] = 1
            print(*tmp)
            break
