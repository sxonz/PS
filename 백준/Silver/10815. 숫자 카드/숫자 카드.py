n = int(input())
d = set(map(int,input().split()))
m = int(input())
for i in list(map(int,input().split())):
    if i in d:
        print(1,end=' ')
    else:
        print(0,end=' ')
