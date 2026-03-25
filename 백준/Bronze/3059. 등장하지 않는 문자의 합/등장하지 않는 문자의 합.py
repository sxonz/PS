for t in range(int(input())):
    s = input()
    ans = 0
    for i in range(65,91):
        if chr(i) not in s:
            ans += i
    print(ans)