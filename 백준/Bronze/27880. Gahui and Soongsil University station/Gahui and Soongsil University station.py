d={"Es":21,"Stair":17}
ans=0
for i,j in [input().split() for _ in range(4)]:
    ans += int(j)*d[i]
print(ans)
    