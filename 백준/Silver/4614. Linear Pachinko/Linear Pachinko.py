while True:
    s = input()
    if s == "#":
        break
    s = list(s)
    n = len(s)
    ans = 0
    poss = 0

    for i in range(n):
        if s[i] == ".":
            ans += 100
            poss = 1
        elif s[i] == "/":
            if i == 0 or s[i-1] == "." or poss:
                ans += 100
            poss = 0
        elif s[i] == "\\":
            if i == n-1 or s[i+1] == ".":
                ans += 100
            elif i < n-1 and s[i+1] == "_":
                s[i+1] = "\\"
            poss = 0
        elif s[i] == "|":
            if i == 0 or s[i-1] == "." or poss:
                ans += 50
            if i == n-1 or s[i+1] == ".":
                ans += 50
            elif i < n-1 and s[i+1] == "_":
                s[i+1] = "|"
            poss = 0
        else:
            if i == 0:
                poss = 1
    print(ans//n)