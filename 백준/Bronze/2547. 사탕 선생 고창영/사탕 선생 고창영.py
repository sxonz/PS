for t in range(int(input())):
    input()
    n = int(input())
    d = [int(input()) for i in range(n)]
    s = sum(d)
    print("YNEOS"[bool(s%n)::2])