n = int(input())
s = input()
cur = [[0,0],[0,0],[0,0],[0,0]]
pos = {"P":0,"A":1,"U":2,"L":3}

for i in range(n):
    if s[i] == "P" and i%2^1:
        cur[0][i%2] = 1
    elif s[i] in pos:
        if cur[pos[s[i]]-1][i%2^1]:
            cur[pos[s[i]]][i%2] = 1

if cur[-1][n%2^1]:
    print("YES")
else:
    print("NO")