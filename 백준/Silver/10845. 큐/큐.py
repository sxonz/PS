import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

queue = deque()
def E():
  return not len(queue)

for i in range(n):
  cmd = input().split()
  
  if cmd[0] == 'push':
    queue.append(cmd[1])

  elif cmd[0] == 'pop':
    print(-1 if E() else queue.popleft())

  elif cmd[0] == 'size':
    print(len(queue))
    
  elif cmd[0] == 'empty':
    print(E()+0)
    
  elif cmd[0] == 'front':
    print(-1 if E() else queue[0])
    
  else:
    print(-1 if E() else queue[-1])