def check(x):
    for i in x:
        if not (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
            return ''
    return x
try:
    r = 0
    while True:
        n = int(input())
        if r:
            print()
        d = dict()
        while True:
            s = input()

            if s == "EndOfText":
                break
            x = []
            tmp = ''
            for i in s:
                if check(i):
                    tmp += i
                else:
                    x.append(tmp.lower())
                    tmp = ''
            x.append(tmp.lower())
            for i in x:
                if i:
                    if i not in d:
                        d[i] = 0
                    d[i] += 1
        flag = True
        for i in sorted(d):
            if d[i] == n:
                flag = False
                print(i)
        if flag:
            print("There is no such word.")
        r += 1
except:
    pass