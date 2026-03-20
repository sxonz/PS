input()
d = set(list(map(int,input().split())))
input()
r = list(map(int,input().split()))
for i in r:
    print(int(i in d))