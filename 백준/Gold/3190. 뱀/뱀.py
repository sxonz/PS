from collections import deque

dx = (0,1,0,-1)
dy = (1,0,-1,0)
R = lambda x:int(x)-1
n = int(input())
k = int(input())
d = {tuple(map(R,input().split())):1 for i in range(k)}
board = [[0]*n for i in range(n)]
board[0][0] = 1
head = (0,0)
tail = deque([(0,0)])
dir = 0

cnt = 0
q = int(input())
tmp = [input().split() for i in range(q)]
query = {i[0]:i[1] for i in tmp}
while True:
	t = tail.popleft()
	cnt += 1
	nx,ny = head[0] + dx[dir], head[1] + dy[dir]
	if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
		head = (nx, ny)
		board[t[0]][t[1]] = 0
		if head in d and d[head]:
			d[head] = 0
			board[t[0]][t[1]] = 1
			tail.appendleft(t)
		board[nx][ny] = 1
		tail.append(head)
	else:
		break
	if str(cnt) in query:
		if query[str(cnt)] == 'L':
			dir = (dir + 3) % 4
		else:
			dir = (dir + 1) % 4

print(cnt)