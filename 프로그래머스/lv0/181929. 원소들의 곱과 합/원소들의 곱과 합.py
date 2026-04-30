def solution(num_list):
    temp = 0
    temp2 = 1
    for i in num_list:
        temp += i
        temp2 *= i
    return 1 if temp ** 2 > temp2 else 0