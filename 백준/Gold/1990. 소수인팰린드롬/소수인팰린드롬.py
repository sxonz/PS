from collections import deque
palindrome = []
queue = deque([''])
for i in range(10):
    queue.append(str(i))

while queue:
    x = queue.popleft()
    if len(x) > 8:
        continue
    if x and x[0] != "0":
        palindrome.append(int(x))
    for i in range(10):
        queue.append(str(i)+x+str(i))

palindrome.sort()
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
a,b = map(int,input().split())
for i in palindrome:
    if a<=i<=b:
        if prime(i):
            print(i)  
print(-1)