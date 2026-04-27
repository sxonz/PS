for t in range(int(input())):
    s = input().split()[::-1]
    print(f"Case #{t+1}: ",end='')
    print(*s)