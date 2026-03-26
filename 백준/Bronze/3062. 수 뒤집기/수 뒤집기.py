for t in range(int(input())):
    n = input()
    tmp = str(int(n)+int(n[::-1]))
    if tmp == tmp[::-1]:
        print("YES")
    else:
        print("NO")
    