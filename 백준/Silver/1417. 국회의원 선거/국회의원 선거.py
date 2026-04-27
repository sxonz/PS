n = int(input())
dasom = int(input())
votes = [int(input()) for _ in range(n-1)]
votes.sort(reverse=True)
cnt = 0
if n == 1:
    print(0)
else:
    while votes[0] >= dasom:
        dasom += 1
        votes[0] -= 1
        cnt += 1
        votes.sort(reverse=True)
    print(cnt)