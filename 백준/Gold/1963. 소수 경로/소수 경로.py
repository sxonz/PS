n=10000
a = [False,False] + [True]*(n-1)
primes=set()

for i in range(2,n+1):
  if a[i]:
    primes.add(str(i))
    for j in range(2*i, n+1, i):
        a[j] = False

from collections import deque

dx = ('0','1','2','3','4','5','6','7','8','9')
testcase = int(input())
for i in range(testcase):
    num1,num2 = map(int,input().split())
    visited = [False]*10000
    visited[num1] = True
    queue = deque([])
    queue.append((str(num1),0))
    while queue:
       x,depth = queue.popleft()
       if x == str(num2):
          print(depth)
          break
       for i in range(4):
          tmp = list(x)
          for j in range(10):
             if j == 0 and i == 0:
                continue
             tmp[i] = dx[j]
             nx = ''.join(tmp)
             if nx in primes and not visited[int(nx)]:
                visited[int(nx)] = True
                queue.append((nx,depth+1))
    else:
       print('impossible')