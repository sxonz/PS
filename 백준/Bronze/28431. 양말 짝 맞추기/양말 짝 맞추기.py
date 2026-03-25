d = [int(input()) for i in range(5)]
for i in d:
    if d.count(i)%2:
        print(i)
        break
        