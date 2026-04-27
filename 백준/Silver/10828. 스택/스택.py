import sys

def stack_commands(commands):

    stack = []

    results = []

    

    for command in commands:

        if command.startswith("push"):

            _, value = command.split()

            stack.append(int(value))

        elif command == "pop":

            if stack:

                results.append(stack.pop())

            else:

                results.append(-1)

        elif command == "size":

            results.append(len(stack))

        elif command == "empty":

            results.append(1 if not stack else 0)

        elif command == "top":

            if stack:

                results.append(stack[-1])

            else:

                results.append(-1)

    

    return results

# Read input

input = sys.stdin.read().strip().split("\n")

N = int(input[0])

commands = input[1:N+1]

# Process commands and get results

results = stack_commands(commands)

# Print results

for result in results:

    print(result)

