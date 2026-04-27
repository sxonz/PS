import sys
sys.setrecursionlimit(1000000)
n = int(input())
nums = [1,5,10,50]
ans = []
sum_set = set()
def dfs(depth,n,idx):
    if depth == n:
        sum_set.add(sum(ans))
    else:
        for i in range(idx,4):
            ans.append(nums[i])
            dfs(depth+1,n,i)
            ans.pop()

dfs(0,n,0)

print(len(sum_set))