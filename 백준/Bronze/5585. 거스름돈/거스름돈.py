n = 1000-int(input())
d = [500,100,50,10,5,1]
ans = 0
for i in d:
    ans += n//i
    n %= i
print(ans)