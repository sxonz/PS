n = int(input())
s = [0 for _ in range(n+1)]
s[3] = 1
if n >= 5:
    s[5] = 1
for i in range(6,n+1):
    temp = s[i-3] +1
    temp2 = s[i-5] +1
    if temp != 1:
        s[i] = temp
    if temp2 != 1:
        if temp != 1:
            s[i] = min(s[i],temp2)
        else:
            s[i] = temp2
if s[n] == 0:
    print(-1)
else:
    print(s[n])