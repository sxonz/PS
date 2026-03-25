for t in range(int(input())):
    n = int(input())
    d = [int(input()) for i in range(n)]
    for i in range(1,max(d)+2):
        s = set()
        for j in d:
            if j%i in s:
                break
            s.add(j%i)
        else:
            print(i)
            break