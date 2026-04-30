def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for idx,v in enumerate(numbers):
        while stack and numbers[stack[-1]] < v:
            answer[stack[-1]] = v
            stack.pop()
        stack.append(idx)
    
    return answer
        

        