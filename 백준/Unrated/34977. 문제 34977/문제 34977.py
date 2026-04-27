n = int(input())
d = list(map(int,input().split()))
for i in range(n//2):
    if d[:i+1] == d[-i-1:]:
        print("yes")
        break
else:
    print("no")