n,m = map(int,input().split())
a = [input() for i in range(n)]
b = [input() for i in range(n)]
for i in range(n):
    tmp = ''
    for j in a[i]:
        tmp += j*2
    if tmp != b[i]:
        print("Not Eyfa")
        break
else:
    print("Eyfa")