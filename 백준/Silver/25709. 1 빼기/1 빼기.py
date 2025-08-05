n = list(input())
cnt = 0
while n:
    if "1" in n:
        n.pop(n.index("1"))
    else:
        n = list(str(int(int(''.join(n))-1)))
    while n and n[0] == "0":
        n.pop(0)
    cnt += 1
print(cnt)