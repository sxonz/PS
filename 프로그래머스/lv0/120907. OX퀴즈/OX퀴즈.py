def solution(quiz):
    result = []
    for i in quiz:
        num1, cal, num2, equal, ans = i.split()
        if eval(num1+cal+num2) == int(ans):
            result.append('O')
        else:
            result.append('X')
    return result
     