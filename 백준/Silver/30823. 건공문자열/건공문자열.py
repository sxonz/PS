n,k = map(int,input().split())
s = input()
tmp = s[:k-1]
if (n-k)%2 == 0:
    tmp = tmp[::-1]
print(s[k-1:]+tmp)