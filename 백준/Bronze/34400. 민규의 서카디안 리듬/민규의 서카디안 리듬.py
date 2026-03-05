for t in range(int(input())):
    n = int(input())
    n %= 25
    if n < 17:
        print("ONLINE")
    else:
        print("OFFLINE")