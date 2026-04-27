import sys
input = sys.stdin.readline
d = {}
for i in range(1,10**6+1,2):
    if i not in d:
        d[i] = "O"
for i in range(10**3+1):
    if i*i in d:
        d[i*i] += "S"
    else:
        d[i*i] = "S"
for i in range(int(input())):
    n = int(input())
    if n not in d:print("EMPTY")
    else: print(d[n])
