while True:
    d = list(map(int, input().split()))
    tc = d[0]
    d = d[1:] + [0]
    if not tc:
        break

    stack = []
    m = 0

    for i in range(tc+1):

        while stack and stack[-1][1] > d[i]:
            idx,v = stack.pop()

            if stack:
                width = i - stack[-1][0] - 1
            else:
                width = i
            m = max(m, width * v)
        stack.append((i,d[i]))
    print(m)