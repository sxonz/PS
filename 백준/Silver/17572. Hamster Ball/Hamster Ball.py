n = float(input())
b = int(input())
d = [tuple(map(int,input().split())) for i in range(b)]
d.sort(key=lambda x:x[1])
cnt = 0
for i in d:
    for j in range(i[0]):
        r = i[1]*2*3.14159265358979323846264338327950288419716939937510
        if n >= r:
            n -= r
            cnt += 1
print(cnt)
