n,m = map(int,input().split())
a = [list(map(int,input())) for i in range(n)]
b = [list(map(int,input())) for i in range(n)]

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] ^ b[i][j]:
            for k in range(3):
                for l in range(3):
                    a[i+k][j+l] ^= 1
            cnt+=1
print(cnt if a==b else -1)