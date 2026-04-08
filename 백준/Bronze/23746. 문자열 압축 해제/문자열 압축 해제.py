n = int(input())
d = dict()
for i in range(n):
    a,b = input().split()
    d[b] = a
s = input()
ans = ''
for i in s:
    ans += d[i]
x,y = map(int,input().split())
print(ans[x-1:y])