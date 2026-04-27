for t in range(int(input())):
    n = int(input())
    d = input().split()
    s = d[0]
    for i in d[1:]:
        if i > s[0]:
            s = s + i
        else:
            s = i + s
    print(s)