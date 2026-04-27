s = input()
cur=ans=0
bef = ""
for i in s:
    if i == "(":
        cur += 1
    else:
        cur -= 1
        if bef == "(":
            ans += cur
    bef = i
print(ans)
