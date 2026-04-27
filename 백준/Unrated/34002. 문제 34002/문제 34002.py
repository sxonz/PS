a,b,c = map(int,input().split())
s,v = map(int,input().split())
l = int(input())*100
t = 0
while l < 25000:
    if v:
        v -= 1
        for i in range(30):
            l += c
            t += 1
            if l >= 25000:
                print(t)
                exit()
    elif s:
        s -= 1
        for i in range(30):
            l += b
            t += 1
            if l >= 25000:
                print(t)
                exit()
    else:
        t += 1
        l += a
        if l >= 25000:
            print(t)
            exit()