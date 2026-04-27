import sys
input = sys.stdin.readline
stack = []
l = 0
for i in range(int(input())):
    q,*r = map(int,input().split())
    if q == 1:
        stack.append(r[0])
        l += 1
    elif q == 2:
        if l:
            print(stack.pop())
            l -= 1
        else:
            print(-1)
    elif q == 3:
        print(l)
    elif q == 4:
        print(min(1,l)^1)
    else:
        if l:
            print(stack[-1])
        else:
            print(-1)
        
