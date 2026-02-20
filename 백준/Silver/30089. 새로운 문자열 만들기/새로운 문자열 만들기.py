for t in range(int(input())):
    s = input()
    for i in range(len(s)):
        tmp = s[i:]
        if tmp == tmp[::-1]:
            print(s[:i]+s[::-1])
            break