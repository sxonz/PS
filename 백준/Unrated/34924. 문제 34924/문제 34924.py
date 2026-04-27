n = int(input())
s = input()
remain = [1]*n
i = 0
while i<n:
    if s[i] not in "PAUL" and i != n-1:
        remain[i] = 0
        remain[i+1] = 0
        i += 1
    i += 1
if ''.join([i for i,j in zip(s,remain) if j]) == "PAUL":
    print("YES")
else:
    print("NO")