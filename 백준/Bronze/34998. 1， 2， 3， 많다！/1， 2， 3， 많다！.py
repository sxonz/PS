for t in range(int(input())):
    n = int(input())
    s = input().split(" + ")
    if "!" in s or sum([int(i) for i in s]) > 9:
        print("!")
    else:
        print(sum([int(i) for i in s]))