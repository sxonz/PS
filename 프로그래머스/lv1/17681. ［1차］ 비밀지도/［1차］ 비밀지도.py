def solution(n, arr1, arr2):
    bin_arr1 = [bin(i).lstrip('0b') for i in arr1]
    bin_arr2 = [bin(i).lstrip('0b') for i in arr2]
    answer = []
    for i in range(n):
        if len(bin_arr1[i]) != n:
            bin_arr1[i] = '0' * (n - len(bin_arr1[i])) + bin_arr1[i]
        if len(bin_arr2[i]) != n:
            bin_arr2[i] = '0' * (n - len(bin_arr2[i])) + bin_arr2[i]
    for i,j in zip(bin_arr1,bin_arr2):
        sum = ''
        for k in range(n):
            if i[k] == '1' or j[k] == '1':
                sum += '#'
            else:
                sum += ' '
        answer.append(sum)
    return answer