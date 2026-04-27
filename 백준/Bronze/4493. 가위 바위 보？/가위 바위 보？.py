win = {"R":"S","S":"P","P":"R"}
for t in range(int(input())):
    n = int(input())
    a,b = 0,0
    for i in range(n):
        x,y = input().split()
        if x == y:
            continue
        if win[x] == y:
            a += 1
        else:
            b += 1
    if a>b:
        print("Player 1")
    elif b>a:
        print("Player 2")
    else:
        print("TIE")