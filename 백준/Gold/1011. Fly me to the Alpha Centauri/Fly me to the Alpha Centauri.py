for _ in range(int(input())):
    x, y = map(int, input().split())
    
    distance = y - x
    cur = cnt = mov = 0

    while cur < distance:
        cnt += 1
        mov += cnt%2
        cur += mov
    print(cnt)