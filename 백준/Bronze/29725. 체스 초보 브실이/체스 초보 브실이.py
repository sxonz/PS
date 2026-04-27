val = {"P":1,"p":-1,"N":3,"n":-3,"B":3,"b":-3,"R":5,"r":-5,"Q":9,"q":-9}
s = [input() for i in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if s[i][j] in val:
            ans += val[s[i][j]]
print(ans)