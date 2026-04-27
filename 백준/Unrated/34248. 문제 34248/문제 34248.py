n = int(input())
d = list(map(int,input().split()))
a = d.count(1)
b = n - a
while a > b:
    a -= 2
    b += 1
if a != b:
    print("No")
else:
    print("Yes")