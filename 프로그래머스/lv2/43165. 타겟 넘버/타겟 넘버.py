def solution(numbers, target):
    count = 0
    stack = []
    stack.append([0,0])
    while stack:
        current,cnt = stack.pop()
        if current == target and cnt == len(numbers):
            count += 1
        if cnt == len(numbers):
            continue
        stack.append([current+numbers[cnt],cnt+1])
        stack.append([current-numbers[cnt],cnt+1])
    return count