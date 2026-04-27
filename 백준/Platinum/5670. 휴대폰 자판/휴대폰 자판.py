def f(key,cur):
    res = 1
    cur = cur[key[0]]
    for i in key[1:]:
        if len(cur) > 1:
            res += 1
        cur = cur[i]
    return res


try:
    while True:

        n = int(input())
        d = dict()
        s = [input() for i in range(n)]
        for i in s:
            cur = d
            for j in i:
                if j not in cur:
                    cur[j] = dict()
                cur = cur[j]
            cur[''] = ''
        ans = 0
        for i in s:
            ans += f(i,d)
        print("%.2f" % (ans/n))
except:
    pass