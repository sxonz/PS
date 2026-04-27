d = [input() for i in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2^1 and d[i][j] == "F":
            ans += 1
print(ans)