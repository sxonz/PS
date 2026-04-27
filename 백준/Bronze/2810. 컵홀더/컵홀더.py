n = int(input())
s = input().replace("LL","LR")
d = [0]*(n+1)
for i in range(n):
    if s[i] == "S":
        if not d[i]:
            d[i] = 1
        elif not d[i+1]:
            d[i+1] = 1
    elif s[i] == "L":
        if not d[i]:
            d[i] = 1
    elif s[i] == "R":
        if not d[i+1]:
            d[i+1] = 1
print(sum(d))
