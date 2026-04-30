def solution(n):
    watermelon = '수박'
    answer = watermelon * (n // 2)
    if n % 2 != 0:
        answer += '수'
    return answer
        