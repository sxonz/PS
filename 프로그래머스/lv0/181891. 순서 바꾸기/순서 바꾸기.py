def solution(num_list, n):
    list1 = num_list[n:]
    list1.extend(num_list[:n])
    return list1