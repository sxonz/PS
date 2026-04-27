n = int(input())
d = set(map(int,input().split()))
if not d-{0}:
    print(1)
    exit()
if 0 not in d:
    print(0)
else:
    for i in range(1,n+1):
        if i not in d:
            print(i+2)
            break