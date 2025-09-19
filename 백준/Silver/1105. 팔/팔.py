a,b = input().split()
r = len(b)
cnt = 0
flag = False
if len(a) == r:
    for i in range(r):
        if a[i] == b[i]:
            if a[i] == "8":
                cnt += 1
        else:
            break
print(cnt)