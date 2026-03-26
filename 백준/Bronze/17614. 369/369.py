ans = 0
for i in range(int(input())+1):
    i = str(i)
    ans += i.count("3") + i.count("6") + i.count("9")
print(ans)