for t in range(int(input())):
    s = input()
    if len(s)%2^1:
        print(s[::2])
        print(s[1::2])
    else:
        print(s[::2]+s[1::2])
        print(s[1::2]+s[::2])