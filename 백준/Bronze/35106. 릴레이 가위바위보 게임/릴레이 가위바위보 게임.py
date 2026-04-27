n = int(input())
d = list(map(int,input().split()))
a = d.count(1)
b = d.count(2)
c = d.count(3)
if a<n:
    print(1)
elif b<n:
    print(2)
else:
    print(3)
if a>n:
    print(1)
elif b>n:
    print(2)
else:
    print(3)