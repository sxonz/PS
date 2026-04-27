n = int(input())
c = 0
i = 1
while n>c:
    c += i
    if n<=c:
        break         
    i += 1
if i%2:
    print(f'{c-n+1}/{i-c+n}')
else:
    print(f'{i-c+n}/{c-n+1}')