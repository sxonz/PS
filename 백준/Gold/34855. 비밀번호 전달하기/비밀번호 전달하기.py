t = int(input())
d = list(map(int,input().split()))

if t == 1:
    tmp = d[::]
    while True:
        tmp = [(i+1)%64 for i in tmp]
        tmp = [i+(i==0)*64 for i in tmp]

        for i in tmp:
            if i in d:
                break
        else:
            break
    print(*tmp)
else:
    tmp = d[::]
    while True:
        tmp = [(i-1)%64 for i in tmp]
        tmp = [i+(i==0)*64 for i in tmp]

        for i in tmp:
            if i in d:
                break
        else:
            break
    print(*tmp)