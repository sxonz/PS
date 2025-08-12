n = int(input())
s = int(input())
p = "IO"*n + "I"
d = input()
cnt = 0
for i in range(s-n):
    if p == d[i:i+n*2+1]:
        cnt += 1
print(cnt)
