n = int(input())
s = [0 for _ in range(n+1)]
for i in range(2,n+1):
    s[i] = s[i-1] + 1
    if i % 2 == 0:
        s[i] = min(s[i],s[i//2] +1)
    if i % 3 == 0:
        s[i] = min(s[i],s[i//3] +1)
print(s[n])