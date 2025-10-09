for test in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    d.sort()
    st = 0
    for i in d:
        if st+1 <= i:
            st += 1
    print(f"Case #{test+1}: {st}")