n,m = map(int,input().split())
r = 0
for i in range(n):
    s = input()
    if "+" in s:
        r += 1
print(r)