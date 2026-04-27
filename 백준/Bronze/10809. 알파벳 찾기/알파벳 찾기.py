s = input()
print(*[s.find(chr(97+i)) for i in range(26)])