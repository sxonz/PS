from collections import deque

def squarefree(x):
    cnt,sqfree = 0,False
    queue = deque([(1,0,1)])
    while queue:
        cur,idx,m = queue.popleft()
        for next in range(idx,l):
            tmp = cur*prime[next]
            if tmp > x:
                break
            sqfree = sqfree or not(x%tmp)
            cnt += x//tmp*m
            queue.append((tmp,next+1,-m))
    return x-cnt,sqfree


prime = []
visited = [False]*100001
for i in range(2,50001):
  if not visited[i]:
    prime.append(i*i)
    k = 2
    while i*k < 100001:
       visited[i*k] = True
       k += 1
l = len(prime)

s,e = 0,1<<32
num = int(input())
while s<e:
   mid = (s+e)//2
   x,free = squarefree(mid)
   if x == num and not free:
      break
   elif x<num:
      s = mid
   else:
      e = mid
print(mid)

    
