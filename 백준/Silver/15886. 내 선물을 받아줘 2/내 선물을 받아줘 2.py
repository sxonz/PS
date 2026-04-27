n = int(input())
s = input()
last = 'W'
cnt = 0
for i in s:
    if i == 'E':
        if last == 'W':
            cnt += 1
    last = i
print(cnt)
