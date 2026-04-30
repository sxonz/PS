def solution(my_string):
    answer = 0
    temp = 0
    for i in my_string:
        if i.isdigit():
            temp = temp * 10 + int(i)
        else:
            answer += temp
            temp = 0
    return answer + temp