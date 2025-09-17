r = 0
for _ in (0,0,0):
    i = input()
    if r:
        r += 1
    if i.isdigit():
        r = int(i)+1
print(r if r%3 and r%5 else "Fizz" if r%5 else "Buzz" if r%3 else "FizzBuzz")