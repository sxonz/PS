n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if set(a) == set(b) and a == b[:n]:
    print("YES")
else:
    print("NO")