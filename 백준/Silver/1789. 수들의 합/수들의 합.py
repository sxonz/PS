n = max(int(input()),2)
cnt = 0
for i in range(1,n):
    n -= i
    if n < 0:
        break
    cnt += 1
print(cnt)