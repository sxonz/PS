while True:
    s = input()
    if s == "#":
        break
    p = s[-1]
    if s.count("1")%2 and p == "e" or s.count("1")%2^1 and p == "o":
        print(s[:-1]+"1")
    else:
        print(s[:-1]+"0")