for t in range(int(input())):
    a,b = input().split()
    if list(sorted(list(a))) == list(sorted(list(b))):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")