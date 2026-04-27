n = [int(i) for i in list(input())]
ans = int(''.join([str(i) for i in sorted(n,reverse=True)])) if (sum(n) % 3 == 0 and 0 in n) else -1
print(ans)