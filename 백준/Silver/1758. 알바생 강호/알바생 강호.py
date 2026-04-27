l=range(int(input()))
print(sum([max(i-j,0)for i,j in zip(sorted([int(input()) for k in l]),l[::-1])]))
