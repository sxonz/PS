n = int(input())
d = list(map(int,input().split()))
if len(set(d)) != n:
    print(0)
else:
    print(1)