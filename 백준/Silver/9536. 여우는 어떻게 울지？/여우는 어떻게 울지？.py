for test in range(int(input())):
    s = input().split()
    while True:
        tmp = input()
        if tmp == 'what does the fox say?':
            break
        r = tmp.split()[2]
        while s and r in s:
            s.pop(s.index(r))
    print(' '.join(s))
