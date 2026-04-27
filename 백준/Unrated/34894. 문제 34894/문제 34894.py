n = int(input())
s = input()
num = {"U":1,"O":2,"S":3,"P":4,"C":5}
d = [0]+[-1]*5
w = list(map(int,input().split()))
for i in range(n):
    if d[num[s[i]]-1] == -1:
        continue
    if d[num[s[i]]] == -1 or d[num[s[i]]] > d[num[s[i]]-1] + w[i]:
        d[num[s[i]]] = d[num[s[i]]-1] + w[i]
print(d[5])