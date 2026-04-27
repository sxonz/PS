temp = input()
if len(set(temp)) == 1:
    print(-1)
elif temp == temp[::-1]:
    print(len(temp)-1)
else:
    print(len(temp))