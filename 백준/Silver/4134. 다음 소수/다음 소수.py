for t in range(int(input())):
    n = int(input())
    if n < 2:
        n = 2
    while True:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                break
        else:
            print(n)
            break
        n += 1
    