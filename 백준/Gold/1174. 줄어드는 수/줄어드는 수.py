import sys
input = sys.stdin.readline

n = int(input())

num = []
ans = []

def check(i):
	if len(num) == 1: return 1
	if num[-2] > i: return 1
	else: return 0

def dfs(depth):
	for i in range(10):
		num.append(i)
		if check(i):
			dfs(depth + 1)
			ans.append(int(''.join(str(x) for x in num)))
		num.pop()
	
dfs(0)
ans.sort()

if n > len(ans): print(-1)
else: print(ans[n-1])