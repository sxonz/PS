for t in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    W = sum([a[i] == "W" and b[i] == "B" for i in range(n)])
    B = sum([a[i] == "B" and b[i] == "W" for i in range(n)])
    print(W+B-min(W,B))
    