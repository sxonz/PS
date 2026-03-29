n = int(input())
d = list(map(int,input().split()))
psum = 0
ans = 0
for i in d:
    ans = max(ans,i-psum)
    psum += i
print(ans)