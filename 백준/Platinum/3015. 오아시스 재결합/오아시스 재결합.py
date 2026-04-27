import sys
input = sys.stdin.readline
n = int(input())
d = [int(input()) for _ in range(n)]
stack = []
cnt = 0
for i in d:
    if not stack:
        stack.append(i)
    else:
        while stack and stack[-1] < i:
            cnt += 1
            stack.pop()
        s = 0
        e = len(stack)-1
        e2 = e+1
        while s<e:
            mid = (s+e)//2
            if stack[mid] == i:
                e = mid
            else:
                s = mid+1
        if stack and stack[e] == i:
            cnt += e2-e
            if e:
                cnt += 1
        else:
            if stack:
                cnt += 1
        stack.append(i)
print(cnt)