d = [input() for i in range(3)]
r = 0
for i in d:
    if r:
        r += 1
    if i.isdigit():
        r = int(i)+1
print(r if r%3 and r%5 else "Fizz" if r%5 else "Buzz" if r%3 else "FizzBuzz")