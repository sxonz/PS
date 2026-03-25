for t in range(int(input())):
    n = int(input())
    s = input()
    n += s.count("c")-s.count("b")
    print(f"Data Set {t+1}:")
    print(n)
    print()
    