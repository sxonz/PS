while True:
    s = input().lower()
    if s == '#':
        break
    tmp = 0
    for i in "aeiou":
        tmp += s.count(i)
    print(tmp)