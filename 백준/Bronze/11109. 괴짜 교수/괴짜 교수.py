ans = []
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    ans+=[(b*c == a+b*d)*2 + (b*c < a+b*d)]
for i in ans:
    print("pddaoor eanslo ltne olptia zrmeaa lt lt ee lr i  z  e"[i::3].strip())