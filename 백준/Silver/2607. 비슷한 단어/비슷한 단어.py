n = int(input())
s = list(input())
answer = 0

for i in range(n-1):
    compare = s[::] 
    cnt = 0

    for w in input():
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)
