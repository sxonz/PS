n = int(input())
a,b,c,d = input(),input(),input(),input()
ans = ''
for i in range(n):
    if a[i] == c[i]:
        if b[i] != d[i]:
            print("htg!")
            exit()
        ans += b[i]
print(ans)