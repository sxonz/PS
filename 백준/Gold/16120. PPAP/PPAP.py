s = input()
stack = []
PPAP = ["P","P","A","P"]
P = "P"
l = 0
for i in s:
    stack.append(i)
    l += 1
    while l > 3 and stack[-4:] == PPAP:
        for _ in range(3):
            stack.pop()
        l -= 3
if 'A' not in stack and l == 1:
    print(''.join(PPAP))
else:
    print("NP")