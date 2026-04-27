t = int(input())
ans,n = divmod(t,5)
ans += [n//2,2,n//2,3,n//2][n]
ans = ans if t not in [1,3] else -1
print(ans)