for t in range(int(input())):
    n = int(input())
    if n %2:
        print(0)
    else:
        n//=2
        print(2**n)