try:
    while True:
        s,t = input().split()
        n = len(s)
        idx = 0
        for i in range(len(t)):
            if s[idx] == t[i]:
                idx += 1
                if idx == n:
                    print("Yes")
                    break
        else:
            print("No")
        
except:
    pass