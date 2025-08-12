s, p = map(int, input().split())
string = list(input())
A, C, G, T = map(int, input().split())

c = [0,0,0,0]
f = {"A":0, "C":1,"G":2,"T":3}


left, right = 0, p-1
for i in string[left:right]:
    c[f[i]] += 1
cnt = 0

while right < s:

    c[f[string[right]]] += 1

    if c[0] >= A  and c[1] >= C and c[2] >= G and c[3] >= T:
        cnt += 1

    c[f[string[left]]] -= 1 
    left += 1
    right += 1

print(cnt)