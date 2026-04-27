def value(k):
    s = 0
    for i in k:
        if i.isdigit():
            s += int(i)
    return (len(k),s,k)
n = int(input())
d = [input() for _ in range(n)]
d.sort(key=value)
print('\n'.join(d))