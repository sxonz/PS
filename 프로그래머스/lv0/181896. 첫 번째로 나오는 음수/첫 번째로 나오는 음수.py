def solution(num_list):
    return -1 if [num_list.index(i) for i in num_list if i < 0] == [] else [num_list.index(i) for i in num_list if i < 0][0]